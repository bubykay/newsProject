from django import template
# from django.template import Library, Node
from django.template.defaultfilters import stringfilter
from django.template.loader import render_to_string
import re

register = template.Library()


def paragraphs(value):
    """
    Turns paragraphs delineated with newline characters into
    paragraphs wrapped in <p> and </p> HTML tags.
    """
    paras = re.split(r'[\r\n]+', value)
    paras = ['<p>%s</p>' % p.strip() for p in paras]
    return '\n'.join(paras)
paragraphs = stringfilter(paragraphs)
register.filter(paragraphs)


@register.filter(name='twitter_handle')
def twitter_handle(handle):
    k = []
    k.insert(0,handle)
    handles = re.findall(r'\@\w+', k[0])
    for r in handles:
        l = k[0].replace(r, f'<a href="https://www.twitter.com/{r}", target ="_blank" >{r}</a>')
        k.insert(0,l)
        k.pop()
    return (k[0])


@register.filter(name='inject_ads')
def inject_ads(value, arg):
    body = ''
    ad_code = render_to_string("../templates/includes/ads/jumia/nigeria.html")
    paragraphs = value.split('\r')
    # print(paragraphs)
    while arg < len(paragraphs):
        paragraphs.insert(arg,ad_code)
        arg += (arg+1)
    for p in paragraphs:
        body += f'<p>{p}</p>'
    return body



# @register.filter
# def get_url(value):
#     b = urlparse(value)
#     url = b.scheme+ '://' + b.netloc+b.path
#     return url

# @register.filter
# def odd(value):
#     if value is None:
#         return '-'
#     else:
#         return value

# @register.filter
# def advice(value):
#     if value == '1 N':
#         k = '1X'
#     elif value == 'N 2':
#         k = 'X2'
#     elif value == None:
#         k = '-'
#     else:
#         k = value
#     return k

# @register.filter
# def advice_str(value):
#     if value == '1 N':
#         k = 'Home or Draw'
#     elif value == 'N 2':
#         k = 'Away or Draw'
#     elif value == '2':
#         k = 'Away'
#     elif value == '1':
#         k = 'Home'
#     elif value == None:
#         k = '-'
#     else:
#         k = value
#     return k



# @register.filter
# def to_int(value):
#     return int(value)

# @register.filter
# def strtotim(value):
#     return datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=pytz.UTC)

# @register.filter
# def plus_day(value, days):
#     return value + datetime.timedelta(days=days)
# @register.filter
# def minus_day(value, days):
#     return  value - datetime.timedelta(days=days)

# @register.filter
# def highlight(value):
#     k = value.split('\r')
#     return k[0]
