from bs4 import BeautifulSoup
import requests
from time import sleep
from lxml import html
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import json
from django.utils.text import slugify
import re

f = open('resource.json') 
f1 = f.read()
resources = json.loads(f1)
f.close()  
session = requests.Session()
retry = Retry(connect=3, backoff_factor=5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

url_link = 'https://punchng.com/2021-proposed-n6tn-loans-pdp-apc-clash-over-fgs-fresh-plans-man-demands-caution/'
page = session.get(url_link)
soup = BeautifulSoup(page.content, 'html.parser')
# regex = re.compile('.* jetpack-lazy-image.*')
# img = soup.find('img', class_=regex).get('src')
body = soup.find('div', class_='entry-content')
# p = body.parent.find_all('p')
# img =  soup.select('div[class*="jetpack-lazy-image"]')
# k = len(p)-1
#     del body[k]
#     body_p = ''
#     for p in body.parent.find_all('p'):
#         body_p += str(p.get_text()) + '\r'
with open('soup1.html', 'w') as f:
    f.write(str(body))
# h2 = soup.find_all(resource['url_loc'], class_=resource['url_class'])
# for l in h2:
#     link= l.find_next('a')
#     if len(str(resource['base'])) > 0:
#         url = resource['base']+link.get('href')
#     else:
#         url = link.get('href') #individual link generation stops here
#     # f.writelines("%s\n" % str(url))
#     scrape = requests.get(url) #content generation starts here
#     url_page = BeautifulSoup(scrape.content, 'html.parser')
#     body = url_page.find('div', class_='entry-content')
#     if body.find('video'):
#         continue #passing video body content
#     if key == 'vanguard':
#         imgsrc = url_page.find('img', class_='aligncenter wp-image-1393483').get('src')
#         # title = url_page.find('h1', class_='entry-title').get_text()
#     elif key == 'punch':
#         imgsrc = url_page.find('div', class_='b-lazy').get('data-src')
#         # title = url_page.find('h1', class_='post_title').get_text()
#     # f.writelines("%s\n" % str(url))
#     # f.writelines(str(key) + ': ' +str(title) + "\n")
#     f.writelines(str(imgsrc) +'\n')
#     f.writelines('===================================================' + '\n')
#     # for p in body.find('p').parent.find_all('p'):
#     #     body_p += str(p) + '\n'
#     imgsrc = ''
    

            #     f.writelines(str(p.get_text())+"\n")
            # f.writelines('+++++++++++++++++++'+"\n"+"\n")
            # counter+=1
        # f.writelines(str(counter))
            
                






