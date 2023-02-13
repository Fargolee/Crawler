#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2023/2/13 22:56
# @File  : music.py
# 【【Python爬虫案例】爬取网易云榜单音乐，批量下载保存到本地】https://www.bilibili.com/video/BV1Wx4y1V7V2?vd_source=a9a448b7b47b7e1eaf4947ec5a479ebc

import requests
from lxml import etree
import os

filename = 'music\\'
if not os.path.exists(filename):
    os.makedirs(filename)

url = 'https://music.163.com/discover/toplist'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers).text
# print(response)

html = etree.HTML(response)
li_list = html.xpath('//ul[@class="f-hide"]/li')
for li in li_list:
    song_name = li.xpath('./a/text()')[0]
    song_id = li.xpath('./a/@href')[0]
    song_id = song_id.split('=')[-1]
    song_url = f'https://music.163.com/song/media/outer/url?id={song_id}'
    print(song_name)

    res = requests.get(song_url, headers=headers).content

    with open(f'music/{song_name}.mp3', 'wb') as f:
        f.write(res)


