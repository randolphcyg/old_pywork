#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Randolph
# datetime:2018/5/29 8:33
# software: PyCharm

import urllib.request
import json
import os

response = urllib.request.urlopen(
    "http://pvp.qq.com/web201605/js/herolist.json")

hero_json = json.loads(response.read())
hero_num = len(hero_json)

# 文件夹不存在则创建
save_dir = os.getcwd() + '\\headskin\\'
if not os.path.exists(save_dir):
    os.mkdir(save_dir)
print('爬取英雄头像开始：')
for i in range(hero_num):
    # 获取英雄头像皮肤列表
    skin_names = hero_json[i]['skin_name'].split('|')

    for cnt in range(len(skin_names)):
        save_file_name = save_dir + str(hero_json[i]['ename']) + '.jpg'
        print('爬取', save_file_name, '完成;')
        # http://game.gtimg.cn/images/yxzj/img201606/heroimg/504/504.jpg
        skin_url = 'http://game.gtimg.cn/images/yxzj/img201606/heroimg/' + str(
            hero_json[i]['ename']) + '/' + str(hero_json[i]['ename']) + '.jpg'
        if not os.path.exists(save_file_name):
            urllib.request.urlretrieve(skin_url, save_file_name)
print('爬取英雄头像完成！')
