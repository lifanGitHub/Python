from util import NetUtil
from util import ViewUtil

sumRead = 0
titleList = []
numList = []


for indexHtml in range(1, 17):
    soup = NetUtil.getBeautifulSoup("https://blog.csdn.net/coder_pig/article/list/%d" % indexHtml)
    # if soup is None:
    #     sys.exit()

    items = soup.find_all(name="div", attrs={"class": "article-item-box csdn-tracking-statistics"})
    for index, item in enumerate(items):
        if index == 0:
            continue
        titleList.append(item.a.contents[2].strip())
        print(item.a.contents[2].strip())

        readNum = item.find_all(name="span", attrs={"class": "num"})[0].string
        numList.append(int(readNum))
        sumRead += int(readNum)
        print("阅读数= " + readNum)

ViewUtil.showChart(titleList,numList)

# print(all_href[1])
# print(all_href[1].a)
# print(all_href[1].a.contents)
# print(all_href[1].a.children)
# for _str in items[1].a.stripped_strings:
#     print(_str)
# print(all_href[1].name)
# print(all_href[1].attrs.get("class")[0])
# print(all_href[1].string)

# def getData():
#     for index, item in enumerate(items):
#         if index == 0:
#             continue
#         titleList.append(item.a.contents[2].strip())
#         print(item.a.contents[2].strip())
#
#         readNum = item.find_all(name="span", attrs={"class": "num"})[0].string
#         numList.append(int(readNum))
#         sumRead += int(readNum)
#         print("阅读数= " + readNum)
#