from asyncio import coroutine, get_event_loop
from requests import get
from bs4 import BeautifulSoup

url_list =[
        'https://www.konami.com/efootball/pt-br/',
        'https://www.primevideo.com/?_encoding=UTF8&language=pt_br',
        'https://g1.globo.com/',
        'https://pt-br.facebook.com/',
        'https://www.rockstargames.com/br/',
        'https://www.playstation.com/pt-br/ps5/',
        'https://sms.playstation.com/',
        'https://www.netflix.com/br/',
        'https://recordtv.r7.com/',
        'https://www.amazon.com.br/'
]

@coroutine
def web_scrape():
    loop = get_event_loop()
    lista = [loop.run_in_executor(None, get, url,) for url in url_list]
    for link in lista:
        resp = yield from link
        print(resp.ok)

loop = get_event_loop()
loop.run_until_complete(web_scrape())

@coroutine
def tese():
    loop = get_event_loop()
    for resp in url_list:
        site = get(resp)
        tags = BeautifulSoup(site.text, 'html5lib')
        titulo = tags.find('title')
        print(f'Titulo da Pagina: {titulo.text}')
        print('Proxima Pagina...')

loop = get_event_loop()
loop.run_until_complete(tese())
