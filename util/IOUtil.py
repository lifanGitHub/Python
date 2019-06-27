import os


def mk_dir(path):
    allPath = os.path.abspath('.') + '\\' + path
    if not os.path.exists(allPath):
        os.makedirs(allPath)
    return allPath + '\\'


if __name__ == '__main__':
    mk_dir('test')
