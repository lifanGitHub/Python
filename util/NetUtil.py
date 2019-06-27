import urllib
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup


def getBeautifulSoup(url, decode='utf-8'):
    try:
        html = urlopen(url).read().decode(decode)
        return BeautifulSoup(html, features='lxml')
    except:
        return None


def getBeautifulSoup3(url, decode='utf-8'):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.103 Safari/537.36'}
        # Request类的实例，构造时需要传入Url,Data，headers等等的内容
        resquest = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(resquest).read()
        return response.decode(decode)
    except:
        return None


def getBeautifulSoup2(url, decode='utf-8'):
    try:
        # 添加头部，伪装浏览器，字典格式
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2883.103 Safari/537.36'}
        # 增加headers参数
        response = requests.get(url=url, headers=headers)
        response.encoding = decode
        return response.text
    except:
        return None
