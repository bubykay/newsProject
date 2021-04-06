from bs4 import BeautifulSoup
import requests
from time import sleep
from lxml import html
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import json


goal = 'http://saharareporters.com/news'
base = 'https://sahararepoters.com/'
session = requests.Session()
retry = Retry(connect=3, backoff_factor=5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)
page = session.get(goal)
soup = BeautifulSoup(page.content, 'html.parser')
h2 = soup.find_all('span', class_='block-module-content-header-title')
with open('news_test.html', 'w') as f:
    for l in h2:
        link= l.find_next('a')
        url = link.get('href')
        f.writelines("%s\n" % str(url))

