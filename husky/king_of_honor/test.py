# -*- coding: utf-8 -*-
# @Time    : 2019/3/23 20:53
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : test.py
# @Software: PyCharm

import requests
import urllib.request

url = 'https://pvp.qq.com/web201605/herolist.shtml'
kv = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/72.0.3626.121 Safari/537.36'}
try:
    r = requests.get(url, headers=kv)

    response = urllib.request.urlopen(
        "http://pvp.qq.com/web201605/js/herolist.json")

    print(response)
    # print(r.status_code)
    # print(r.encoding)
    # print(r.apparent_encoding)
    # print(r.request.headers)
    # print(r.text[:])
    # r.encoding = r.apparent_encoding
except BaseException:
    print('Running Failed!')

#  ________       ___    ___   ________
# |\   ____\     |\  \  /  /| |\   ____\
# \ \  \___|     \ \  \/  / | \ \  \___| _____
#  \ \  \         \ \    / /   \ \  \   |\____\
#   \ \  \____     \/  /  /     \ \  \  |_| \  \
#    \ \_______\ __/  / /        \ \  \___\__\  \
#     \|_______||\___/ /          \ \_________\  \
#               \|___|/            \|____________|
