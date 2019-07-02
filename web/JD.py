import urllib.request

from bs4 import Tag

from util import NetUtil, IOUtil


def main():
    soup = NetUtil.getBeautifulSoup('http://www.shihuo.cn/search?keywords=AJ&channelType=10#qk=SearchAllZB&order=4&type=1')
    print(soup)
    # items = soup.find(name='ol', attrs={'class': 'grid_view'})
    # for index, item in enumerate(items):
        # print(type(item))
        # if not isinstance(item, Tag):
        #     continue
        # imageItem = item.find(attrs={'class': 'pic'}).a.img
        # name = imageItem['alt']
        # src = imageItem['src']
        # print(name + src)
        # path = IOUtil.mk_dir('img')
        # urllib.request.urlretrieve(src, path + '%s.png' % name)


if __name__ == '__main__':
    main()
