'''
Multithreading for I/0 bound Tasks
Scenario - Web Scraping
Web Scraping involves making numerous network requests to fetch web pages. 
These tasks are I/0 bound because they spend a lot of
time waiting for responses from server.
Multithreading can significantly improve the performance by allowing
multiple web pages to be fetched concurrently.
'''

import threading
import requests
from bs4 import BeautifulSoup

urls={
    "https://developer.mozilla.org/en-US/docs/Web/JavaScript"
    "https://javascript.info/"
    "https://www.w3schools.com/js/DEFAULT.asp"
}

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')

threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched")


