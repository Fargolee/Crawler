import os
import requests
import re

for i in range(0, 10):
    if i == 0:
        i = ''
    elif i != 0:
        i = '_' + str(i)
    else:
        pass
    # print(i)

    mulu_url = f'https://www.3gbizhi.com/meinv/bjnmn{i}.html'

    # mulu_url = 'https://www.3gbizhi.com/meinv/mnxz.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    mulu_yuanma = requests.get(mulu_url).text
    taotu_list = re.findall('<a href="(.*)" target="_blank" class="imgw" title="(.*)">',mulu_yuanma)
    for taotu_info  in  taotu_list:
        taotu_dizhi, taotu_name = taotu_info
        filename = taotu_name + '\\'
        if not os.path.exists(filename):
            os.mkdir(filename)


        # taotu_url = 'https://www.3gbizhi.com/meinv/mn1796_2.html'

        taotu_yuanma = requests.get(taotu_dizhi,headers=headers).text
        # print(taotu_yuanma)
        # img_url = re.findall('<img src="(.*)">',taotu_yuanma)[2:-1]
        img_list= re.findall('<img src="(.*.jpg)">',taotu_yuanma)
        # print(img_list)
        flag = 0
        for img_url_re in img_list:
            img_url = img_url_re.replace('thumb_200_0_', '')
            flag += 1
            print(taotu_name,img_url)
            # img_tile = img_url.split('/')[-1]

            with open(filename+str(flag)+'.jpg', 'wb') as f:
                tu = requests.get(url = img_url).content
                f.write(tu)
