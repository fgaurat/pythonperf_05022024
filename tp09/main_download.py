import requests
from bs4 import BeautifulSoup
from pprint import pprint

import time

def main():
    start = time.perf_counter()
    root_url = "https://logs.eolem.com"
    response = requests.get(root_url)

    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = soup.find_all('a')

    links = [a['href'] for a in all_a if ".log" in a['href']]

    for link in links:
        url = f"{root_url}/{link}"
        response = requests.get(url)
        with open(f"tp09/{link}","w") as f:
            f.write(response.text)
            # print(response.text,file=f)
    end = time.perf_counter()

    print(f"time : {end-start:.2f} s")
if __name__=='__main__':
    main()
