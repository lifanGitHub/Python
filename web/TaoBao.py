# coding=gbk
from util import NetUtil


def main():
    soup = NetUtil.getBeautifulSoup2(
        'https://molifang.world.tmall.com/search.htm?spm=a312a.7700824.w10338161-15981313681.4.54a267danIjmQ3&search=y',
        decode='gbk')
    # print(soup.body.prettify())
    # print(soup.prettify())
    t = soup.find_all(attrs={'class': 'eshop head-expand tb-shop'})
    print(t[0].prettify())
    # items = soup.find_all(name='div', attrs={'class': 'item5line1'})
    # readNum = soup.body.find_all(name="a", attrs={"class": "J_TGoldData"})
    # items = soup.find_all(name='div')
    # print(readNum)


if __name__ == '__main__':
    main()
