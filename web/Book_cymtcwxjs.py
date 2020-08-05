import urllib.request

from bs4 import Tag, NavigableString

from util import NetUtil, IOUtil


def main():
    soup = NetUtil.getBeautifulSoup2('http://www.yuedu88.com/chanyumotuocheweixiuyishu/30056.html',decode="GBK")
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
            resultList.append("\n<class 'dict'>: {'*': ['class', 'accesskey', 'dropzone'], 'a': ['rel', 'rev'], 'link': ['rel', 'rev'], 'td': ['headers'], 'th': ['headers'], 'form': ['accept-charset']")

    print("".join(resultList))

if __name__ == '__main__':
    main()
