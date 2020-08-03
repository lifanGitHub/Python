from bs4 import NavigableString

from util import NetUtil
from util import PrintUtil as ps

def main():
    index = 158626 + 9
    url = 'https://www.kanunu8.com/book3/7152/' + str(index) + '.html'
    print(url)
    soup = NetUtil.getBeautifulSoup2(url, decode="GBK")
    items = soup.find(name='td', attrs={'width': '820'})
    # print(items.contents[1].contents)

    resultList = []
    for index, item in enumerate(items.contents[1].contents):
        # print(type(item))
        if isinstance(item, NavigableString):
            st = str(item)
            # 100以上的字符串换行
            if len(st) > 100:
                st = st[:99] + "\n" + st[100:]
            resultList.append(st)

    ps.print_string("".join(resultList),60)


if __name__ == '__main__':
    main()
