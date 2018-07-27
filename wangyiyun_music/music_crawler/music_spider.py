# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "2018/4/30 下午10:53"

import re
import requests
from bs4 import BeautifulSoup
import json

shanghaidict = {'10952': '周璇', '8388': '李香兰', '7174': '白虹', '7160': '白光', '10307': '姚莉', '226584': '王人美'}

gaigedate = {'10611': '郑绪岚' ,'5387':'王洁实','7238 ':'程琳','7281':'成方圆','9342':'孙青','10589':'张蔷','10728':'朱明瑛','9296':'沈小岑'}

xibeifengdate={'3688':'刘欢','9632':'韦唯','7960':'胡月','7964':'杭天琪','2171':'陈汝佳','8921':'毛阿敏','7709':'范琳琳'}

yaogun ={'2111':'崔健','4968':'孙国庆','11759':'黑豹乐队','12972':'唐朝乐队','6453':'张震岳','5770':'许巍','11127':'beyond','5779':'薛岳','5354':'伍佰'}

xinshengdai ={'4486':'毛宁','7233':'陈明','10635':'周艳泓','9061':'那英','7234':'陈琳','10206':'杨钰莹','5849':'谢东','9294':'孙悦','7308':'陈红','2856':'高枫'}

xiaoyuan={'3713':'李双泽' ,'6073':'杨弦','6086':'叶佳修', '3718':'刘文正', '3714':'李建复','4731':'潘安邦','9167':'齐豫','3682':'老狼' ,'4937':'沈庆' ,'6065':'郁冬'}

huayuliuxing={'6452':'周杰伦', '5196':'陶喆','5346':'王力宏','4723':'潘玮柏' ,'3684':'林俊杰','2738':'方大同','7219':'蔡依林' ,'12709':'SHE' ,'10562':'张韶涵', '6472':'张杰','9269':'容祖儿' ,'8325':'梁静茹','13193':'五月天','5771':'许嵩' ,'8926':'莫文蔚'}

yueyu={'3698':'罗文','10594':'甄妮','3691':'刘德华','6460':'张学友','5782':'许冠杰','5773':'谢霆锋','5205':'谭咏麟', '6457':'张国荣', '8918':'梅艳芳',  '7225':'陈慧娴', '10209':'叶倩文', '2116':'陈奕迅'}

minnan={'6098':'叶启田' , '7346':'陈小云', '7914':'黄乙玲', '7280':'陈盈洁' ,'8418':'林姗' ,'7923':'黄思婷','8437':'龙千玉','2137':'蔡小虎','5389':'王识贤'}



def down_load(kwargs=None,file_name=None):

    for key,value in kwargs.items():
        data = {"id": key}  # 将歌手ID作为params参数传入requests.get()方法
        s_url = "http://music.163.com/artist"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36",
             'Referer': 'http://music.163.com/',
             'Host': 'music.163.com',
        }
        req = requests.get(url=s_url, headers=headers, params=data)  # 请求方式为get。在get请求中，允许使用params关键字，以一个字典来传递这些参数
        req.encoding = "utf-8"
        soup = BeautifulSoup(req.text, "lxml")  # 对返回的数据进行解析,lxml解析器，速度快，健壮性好
        song_list = soup.find_all("ul", class_="f-hide")  # 找到class="f-hide"的<ul>标签
        song_soup = BeautifulSoup(str(song_list), "lxml")  # 将<ul>......</ul>再解析一次，以便使用find_all()方法把所有<a>标签取出来
        song_list = song_soup.find_all("a")
        id_list = []  # 存歌曲ID
        song_name_list = []  # 存歌名

        for each in song_list:
            s_id = each.get("href")  # 歌曲ID在<a>标签href属性中
            s_name = each.string
            s = re.findall(r"\d+", s_id)  # 用正则找到href中的ID
            id_list.append(s[0])  # 由于re.findall()返回的是一个列表，所以用下标将ID取出
            song_name_list.append(s_name)
        file_path = '/Users/purelove/LjcSpider/music_crawler/{0}/{1}.txt'.format(file_name,value)
        for song_id in id_list:
            lrc_url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(song_id) + '&lv=1&kv=1&tv=-1'
            lyric = requests.get(lrc_url)
            import time
            time.sleep(8)
            json_obj = lyric.text
            j = json.loads(json_obj)
            try:
                f = open(file_path, 'a+')
                if j['code'] == 200:
                    lrc = j['lrc']['lyric']
                    pat = re.compile(r'\[.*\]')
                    lrc = re.sub(pat, "", lrc)
                    lrc = lrc.strip()
                    print(str(lrc))
                #file_name = '/Users/purelove/LjcSpider/music_crawler/{}/{}.txt'.format(value)
                    for each in lrc:
                        f.write(each)
                    print(song_id+'写入成功')
                    f.write("\n\n\n")
                    f.close()
                    time.sleep(5)
            except:
                print(str(song_id) + "api访问错误")
                continue


    return '完成'







if __name__ == "__main__":
    #print("上海时期"+down_load(type_id=1,type_name="上海时期",kwargs=shanghaidict,file_name="song_shanghai"))
    print("改革开放初期"+down_load(type_id=2,type_name='改革开放初期',kwargs=gaigedate,file_name="song_gaige"))
    #print("西北风"+down_load(type_id=3,type_name='西北风',kwargs=xibeifengdate,file_name="song_xibeifeng"))
    #print("中国摇滚"+down_load(type_id=4,type_name='中国摇滚',kwargs=yaogun,file_name="song_yaogun"))
    #print("校园歌曲、民谣"+down_load(type_id=6,type_name='校园歌曲、民谣',kwargs=xiaoyuan,file_name="song_xiaoyuan"))
    #print("华语流行"+down_load(type_id=7,type_name='华语流行',kwargs=huayuliuxing,file_name="song_liuxing"))
    #print("粤语"+down_load(type_id=8,type_name='粤语',kwargs=yueyu,file_name="song_yueyu"))
    #print("闽南语"+down_load(type_id=9,type_name='闽南语',kwargs=minnan,file_name="song_minnanyu"))
