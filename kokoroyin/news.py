import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kokoroyin.settings")
django.setup()
from web.models import ScrapedNews
from bs4 import BeautifulSoup
import requests
from time import sleep
from lxml import html
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import json
from keywords import gen_keyword
from django.utils.text import slugify
import KokoRoyin





f = open('resource.json') 
f1 = f.read()
resources = json.loads(f1)
f.close()  
session = requests.Session()
retry = Retry(connect=3, backoff_factor=5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)
for key, resource in resources.items():
    counter = 0
    imgsrc=''
    body_p = ''
    page = session.get(resource['url_link'])
    soup = BeautifulSoup(page.content, 'html.parser')
    h2 = soup.find_all(resource['url_loc'], class_=resource['url_class'])
    for l in h2:
        link= l.find_next('a')
        if len(str(resource['base'])) > 0:
            url = resource['base']+link.get('href')
        else:
            url = link.get('href') #individual link generation stops here
        scrape = requests.get(url) #content generation starts here
        url_page = BeautifulSoup(scrape.content, 'html.parser')
        body = url_page.find('div', class_='entry-content')
        if body.find('video'):
            # print('video present in the content')
            continue #passing video body content
        if key == 'vanguard':
            try:     
                imgsrc = KokoRoyin.get_vanguard_img(body)
                body_p = KokoRoyin.get_vanguard_body(body)
                title = url_page.find('h1', class_='entry-title').get_text()
            except:
                # print(f'there was an exception at: {url}')
                raise
        elif key == 'punch':
            try:
                imgsrc = KokoRoyin.get_punch_img(url_page)
                body_p = KokoRoyin.get_punch_body(body)
                title = url_page.find('h1', class_='post_title').get_text()
            except:
                # print(f'something is wrong @ {url}')
                raise
        if len(body_p) < 50:
            # print(f'Arrghh!! body for url below not scraped:' , '\n', url)
            continue
        if not imgsrc:
            # print(f'Arrghh!! Image link for url below not scraped:' , '\n', url)
            continue
        slug = slugify(title)
        keyword = gen_keyword(title + ' ' +  body_p )
        try:
            new_news, created = ScrapedNews.objects.get_or_create(title=title, body=body_p, keywords=str(keyword), source=key, image=imgsrc, defaults={'slug':slug})
            if created:
                counter += 1
                print(f'{counter} new entry created from: {key}')
            else:
                print('Entry exist')
        except:
            print(f'duplicate entry at: {url} avoided')
            continue
        body_p =''






