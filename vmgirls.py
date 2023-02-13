#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2023/2/11 21:08
# @File  : vmgirls.py
import os

import requests
import re

for i in range(1,101):
    vm_url = f"https://www.vmgirls.net/page/{i}"
    # print(vm_url)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    index_data = requests.get(vm_url,headers=headers).text
    # print(index_data)
    index_info = re.findall('<a class="media-content" href="(.*?)" title="(.*?)"',index_data)
    # print(index_info)
    for tu_info in index_info:
        tu_url,tu_name = tu_info
        filename = tu_name + '\\'
        if not os.path.exists(filename):

            os.mkdir(filename)

        tu_data = requests.get(tu_url,headers=headers).text
        img_url_list = re.findall('<a href="(.*?)" alt=".*?" title=".*?">',tu_data)
        flag = 0
        for img_url in img_url_list:
            img_data = requests.get(img_url, headers=headers).content
            print(tu_name,img_url)
            flag += 1
            with open(filename+str(flag) + '.jpg','wb') as f:
                f.write(img_data)