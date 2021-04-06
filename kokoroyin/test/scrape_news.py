from bs4 import BeautifulSoup
from time import sleep
from lxml import html
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


lnk = 'https://www.vanguardngr.com/2020/10/endsars-ecowas-calls-for-dialogue-to-end-unrest/'
scrape = requests.get(lnk)
soup = BeautifulSoup(scrape.content, 'html.parser')
# title = soup.find('h1', class_='post_title').get_text() #punch
# title = soup.find('h1', class_='entry-title').get_text() #vanguard
# imgsrc = soup.find('img', class_='aligncenter wp-image-1393483').get('src') #for vanguard
# imgsrc = soup.find('div', class_='b-lazy').get('data-src') #.find_next('img').get('src') for punch
body = soup.find('div', class_='entry-content')

# with open('body.html', 'w') as f:
#     f.write(str(title))

with open('scrape_content1.html', 'w') as f:
    f.write(str(body))

# with open('body.html', 'w') as f:
#     f.writelines('Tile is: '+str(title) + "\n")
#     f.writelines(str(imgsrc) +'\n')
#     f.writelines('===================================================' + '\n')
#     for p in body.find('p').parent.find_all('p'):
#         f.writelines(str(p.get_text())+"\n")