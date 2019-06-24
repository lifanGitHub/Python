from urllib.request import urlopen

from bs4 import BeautifulSoup


def getBeautifulSoup(url):
    try:
        html = urlopen(url).read().decode('utf-8')
        return BeautifulSoup(html, features='lxml')
    except:
        return None
