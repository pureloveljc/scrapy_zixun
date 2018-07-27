# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "2018/5/1 下午9:43"


import pymysql




for k,v in minnan.items():
    conn = pymysql.connect(host="127.0.0.1", user="root", passwd="purelove", db="home_scrapy", charset="utf8")
    cursor = conn.cursor()
    file_path ='/Users/purelove/LjcSpider/music_crawler/song_minnanyu/{}.txt'.format(v)
    print(k)
    print(type(k))
    with open(file_path) as f:
        lines = f.readlines()
        lines=''.join(lines).replace('\n','')
        print(lines)
        cursor.execute("insert into all_music(singer_id,singer_name,type_name,all_songs) values(%s, %s,%s,%s)", (k ,v,'闽南语',lines))
        print('success')
        conn.commit()
# print("写入成功")