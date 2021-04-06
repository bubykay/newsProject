from bs4 import BeautifulSoup, NavigableString, Tag
import re

def get_punch_img(soup):
    img = soup.find('div', class_='b-lazy').get('data-src')
    return img

def get_vanguard_img(soup):
    return soup.find('img').get('data-lazy-src')
    

def get_punch_body(body):
    para = body.parent.find_all('p')
    para.pop(0)
    body_p = ''
    for p in para:
        p_low = str(p).lower()
        if 'READ ALSO'.lower() in p_low:
            continue
        elif 'Copyright PUNCH'.lower() in p_low:
            print('copyright met and avoided')
            pass
        elif 'All rights reserved'.lower() in p_low:
            print('All rights reserved met and avoided')
            pass
        elif 'email protected'.lower() in p_low:
            print('email protected met and avoided')
            pass
        else:
            body_p += str(p.get_text()) + '\r'
    return body_p


def get_vanguard_body(body):
    para = body.parent.find_all('p')
    k = len(para)-1
    para.pop(k)
    body_p = ''
    for p in para:
        body_p += str(p.get_text()) + '\r'
    return body_p