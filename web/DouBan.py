import os
import urllib.request

from util import NetUtil


def main():
    soup = NetUtil.getBeautifulSoup('https://movie.douban.com/top250?filter=')
    items = soup.find(name='ol', attrs={'class': 'grid_view'})
    for index, item in enumerate(items):
        if index == 1:
            imageItem = item.find(attrs={'class': 'pic'}).a.img
            name = imageItem['alt']
            src = imageItem['src']
            print(name + src)
            urllib.request.urlretrieve(src, os.path.abspath('.')+'/1.png')


if __name__ == '__main__':
    main()

