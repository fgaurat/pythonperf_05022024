import requests
from bs4 import BeautifulSoup
from pprint import pprint

import time
import threading
import os

import concurrent.futures


def download(link):
    log_file = link.split('/')[-1]
    download_dir = "./tp09/logs"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    response = requests.get(link)
    with open(f"{download_dir}/{log_file}","w") as f:
        f.write(response.text)

def download2(p):
    url,log_file = p
    download_dir = "./tp09/logs"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    response = requests.get(url)
    with open(f"{download_dir}/{log_file}","w") as f:
        f.write(response.text)



def main():
    start = time.perf_counter()
    root_url = "https://logs.eolem.com"
    response = requests.get(root_url)

    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = soup.find_all('a')

    # urls = [f"{root_url}/{a['href']}" for a in all_a if ".log" in a['href']]

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        params = [(f"{root_url}/{a['href']}",a['href']) for a in all_a if ".log" in a['href']]
        executor.map(download2,params)
        
    end = time.perf_counter()

    print(f"time : {end-start:.2f} s")
if __name__=='__main__':
    main()
