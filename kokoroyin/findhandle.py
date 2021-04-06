import re
def twitter_handle(handle):
    k = []
    k.insert(0,handle)
    handles = re.findall(r'\@\w+', k[0])
    for r in handles:
        l = k[0].replace(r, f'<b>{r}</b>')
        k.insert(0,l)
        k.pop()
    return (k[0])


print(twitter_handle('I am kayode and my handle is @femijobi'))