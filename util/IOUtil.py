import os


def mk_dir(path):
    allPath = os.path.abspath('.') + '\\' + path
    if not os.path.exists(allPath):
        os.makedirs(allPath)
    return allPath + '\\'


def write_text(str, name='test.txt', decode='utf-8'):
    with open(name, "w", encoding=decode) as f:
        f.write(str)


def write_binary(str, name='binary.txt'):
    with open(name, "wb") as f:
        f.write(str)


if __name__ == '__main__':
    # mk_dir('test')
    # write_text(NetUtil.getBeautifulSoup2(
    #     "https://molifang.world.tmall.com/search.htm?spm=a312a.7700824.w10338161-15981313681.4.54a267danIjmQ3&search=y",decode='gbk')
    #     .prettify().__str__().encode("gbk",'ignore'), decode='gbk')
    pass
