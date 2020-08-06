from util import NetUtil
from util import PrintUtil
import re

if __name__ == '__main__':
    url = 'https://shsgay.blogspot.com/2019/12/blog-post.html?m=1'
    soup = NetUtil.getBeautifulSoup2(url, decode="utf-8")
    # print(soup)

    items = soup.find_all(attrs={"class": "post-count-link"})
    titleUrlList = []
    for it in items:
        titleUrlList.append(it.attrs['href'])

    str = '20../../'
    url = titleUrlList[0]
    soup = NetUtil.getBeautifulSoup2(url, decode="utf-8")
    print(soup.find_all(attrs={"class": "posts hierarchy"}))




    pass
    # dateUrlList =
    # endTitle = str(soup.find(name='h1', attrs={'id': 'endTitle'}).contents[0].contents[0])
    # print("下载小说《{}》开始...".format(endTitle))
    # div1 = items.contents[1].contents
    # result = "" + str(div1[1]) + str(div1[3]) + str(div1[7]) + str(div1[9])
    # for i in range(2, 1024):
    #     index = "_" + str(i)
    #     url = 'https://www.sztz.org/wenxue/jun/200811/8718' + index + '.html'
    #     soup = NetUtil.getBeautifulSoup2(url, decode="GBK")
    #     items = soup.find(name='div', attrs={'id': 'endText'})
    #     if items is None or items.contents[3] is None:
    #         break
    #     s = str(items.contents[3])
    #     result = result + s
    #     print("下载" + url + "成功" + " 长度 " + str(len(s)))
    # result = result.replace("<p>", "")
    # result = result.replace("</p>", "")
    # result = result.replace("<br>", "")
    # result = result.replace("<br/>", "\n") + "\n"
    # PrintUtil.save_string(result, "{}.txt".format(endTitle))
    # print("保存《{}》成功 总长度{}".format(endTitle, len(result)))
