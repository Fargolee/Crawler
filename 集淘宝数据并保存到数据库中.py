#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2023/2/12 22:55
# @File  : taobao.py
# 【Python爬虫实战：采集淘宝数据，并保存到数据库中】https://www.bilibili.com/video/BV1zt4y1g7kH?vd_source=a9a448b7b47b7e1eaf4947ec5a479ebc
import pymysql
import requests
import re
import json
import csv


def save_sql(title, view_price, item_loc, nick, pic_url, detail_url):
    con = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root',
        db='test'
    )
    db = con.cursor()
    sql = f"insert into goods (title, view_price,  item_loc, nick, pic_url, detail_url) values ('{title}','{view_price}', '{item_loc}','{nick}', '{pic_url}','{detail_url}')"
    # sql = 'insert into goods (title, view_price,  item_loc, nick, pic_url, detail_url) values (1,2,3,4,5,6)'
    db.execute(sql)
    con.commit()
    db.close()


url = 'https://s.taobao.com/search?q=%E5%B7%B4%E9%BB%8E%E4%B8%96%E5%AE%B6&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20230212&ie=utf8'

headers = {
    'cookie': '',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'referer': 'https://s.taobao.com/search?q=iPhone13&suggest=history_1&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.jianhua.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306&_input_charset=utf-8&wq=&suggest_query=&source=suggest'
}
with open('淘宝.csv', 'a', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['title', 'view_price', 'item_loc', 'nick', 'pic_url', 'detail_url'])

response = requests.get(url=url, headers=headers).text
html_data = re.findall('g_page_config = (.*);', response)[0]
# print(html_data)
json_dict = json.loads(html_data)
auctions = json_dict['mods']['itemlist']['data']['auctions']
# print(auctions)
for auction in auctions:
    title = auction['raw_title']
    pic_url = auction['pic_url']
    detail_url = auction['detail_url']
    view_price = auction['view_price']
    item_loc = auction['item_loc']
    nick = auction['nick']
    print(title, view_price, detail_url, item_loc, nick, pic_url)
    save_sql(title=title, view_price=view_price, item_loc=item_loc, nick=nick, pic_url=pic_url, detail_url=detail_url)

    with open('淘宝.csv', 'a', encoding='utf-8', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([title, view_price, item_loc, nick, pic_url, detail_url])
