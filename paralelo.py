from multiprocessing import Pool
from requests import get
from bs4 import BeautifulSoup

url_list =[
        'https://www.konami.com/efootball/pt-br/',
        'https://www.primevideo.com/',
        'https://g1.globo.com/',
        'https://pt-br.facebook.com/',
        'https://www.rockstargames.com/br/',
        'https://www.playstation.com/pt-br/ps5/',
        'https://sms.playstation.com/',
        'https://www.netflix.com/br/',
        'https://recordtv.r7.com/',
        'https://www.amazon.com.br/'
]

def scraper(url):
    site = get(url)
    tags = BeautifulSoup(site.text, 'html5lib')
    titulo = tags.find('title')
    return titulo.text


if __name__ == '__main__':
    s = Pool(10)
    resul = s.map(scraper, url_list)
    print(resul)
