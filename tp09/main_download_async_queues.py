import requests
from bs4 import BeautifulSoup
from pprint import pprint
import asyncio
import time
import os
import httpx
import aiohttp

async def download(download_queue:asyncio.Queue,save_queue:asyncio.Queue):
    while True:
        url = await download_queue.get()
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                text = await response.text()
                log_file = url.split('/')[-1]
                download_dir = "./tp09/logs"
                d = {
                    "text":text,
                    "log_file":log_file,
                    "download_dir":download_dir
                    
                }
                save_queue.put_nowait(d)
        download_queue.task_done()

async def save(save_queue:asyncio.Queue):
    while True:
        save_data = await save_queue.get()
        text = save_data['text']
        log_file = save_data['log_file']
        download_dir = save_data['download_dir']
        with open(f"{download_dir}/{log_file}","w") as f:
            f.write(text)
        save_queue.task_done()



async def main():
    start = time.perf_counter()
    download_queue = asyncio.Queue()
    save_queue = asyncio.Queue()
    nb_download_workers = 10
    nb_save_workers = 5

    root_url = "https://logs.eolem.com"
    response = requests.get(root_url)

    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = soup.find_all('a')

    links = [f"{root_url}/{a['href']}" for a in all_a if ".log" in a['href']]

    tasks =[]

    for i in range(nb_download_workers):
        task = asyncio.create_task(download(download_queue,save_queue))
        tasks.append(task)


    for i in range(nb_save_workers):
        task = asyncio.create_task(save(save_queue))
        tasks.append(task)

    for link in links:
        print(link)
        download_queue.put_nowait(link)

    await download_queue.join()
    await save_queue.join()

    [task.cancel() for task in tasks]

    end = time.perf_counter()

    print(f"time : {end-start:.2f} s")

if __name__=='__main__':

    asyncio.run(main())
