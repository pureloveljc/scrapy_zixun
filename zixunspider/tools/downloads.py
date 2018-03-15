# -*- coding: utf-8 -*-
__time__ = '2018/3/13 0013'
__author__ = 'purelove'

import pymysql
from urllib import  request
import urllib
db = pymysql.connect("localhost","root","purelove","spider",charset='utf8' )
cursor = db.cursor()
cursor.execute("select * from jianzhu_xueyuan where one_class='国家规范' and  two_class not in('城市规划' ,'给水排水','建筑专业','结构专业','暖通空调','道路桥梁','电气专业')")
#cursor.execute("select * from jianzhu_xueyuan where one_class='其它资源' ")
data = cursor.fetchall()
# data =cursor.fetchone()
data_list=list(data)
print(type(data_list))
l=[]
for x in data_list:
    print(x)
    def getFile(url):
        try:
            file_name ='E:\\'+x[5]+'_'+x[6]+'_'+x[0]+'_'+url.split('/')[-1]
            u = urllib.request.urlopen(url)
            f = open(file_name, 'wb')
        except:
            print("错误")
        else:
            block_sz = 8192
            while True:
                buffer = u.read(block_sz)
                if buffer:
                    f.write(buffer)
                else:
                    break
            print ("Sucessful to download" + " " + file_name)
    getFile(x[4])