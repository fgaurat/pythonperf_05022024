import requests
from bs4 import BeautifulSoup
from pprint import pprint

import time
import threading
import os



def download(link):
    log_file = link.split('/')[-1]
    download_dir = "./tp09/logs"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    response = requests.get(link)
    with open(f"{download_dir}/{log_file}","w") as f:
        f.write(response.text)



def main():
    start = time.perf_counter()
    root_url = "https://logs.eolem.com"
    response = requests.get(root_url)

    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = soup.find_all('a')

    links = [a['href'] for a in all_a if ".log" in a['href']]

    threads = []
    for link in links:
        url = f"{root_url}/{link}"
        th = threading.Thread(target=download,args=[url])
        threads.append(th)

    [th.start() for th in threads]
    
    [th.join() for th in threads]

    end = time.perf_counter()

    print(f"time : {end-start:.2f} s")
if __name__=='__main__':
    main()
