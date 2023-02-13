#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2023/2/11 21:54
# @File  : 16k.py
import os

import requests
import re

flag = 0
for i in range(1,192):
    k_url = f"https://www.16k.club/index.php?p={i}"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    index_data = requests.get(k_url,headers=headers).text
    # print(index_data)
    index_info = re.findall('<img src="(.*?)" data-src=".*?" alt="(.*?)"',index_data)
    # print(index_info)

    for tu_info in index_info:
        tu_url,tu_name = tu_info
        flag += 1
        img_title = tu_name+ str(flag)+'.' + tu_url.split('.')[-1]
        print(img_title)
        filename = '16k\\'
        if not os.path.exists(filename):
            os.mkdir(filename)

        img = requests.get(tu_url,headers=headers).content
        with open(filename+img_title, 'wb') as f:
            f.write(img)