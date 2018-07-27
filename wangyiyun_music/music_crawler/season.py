# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = '2018/5/14 16:13'
import jieba
from collections import Counter

def word_list(path):
    with open(path,'r',encoding='UTF-8') as file:
        lyric_str = file.read()
        seg=jieba.cut(lyric_str)#jieba分词
        word_list=[]
        word_dict={}
        for each in seg:
            #print(each+' ')
            if len(each)>1:#过滤长度为1的词
                word_list.append(each)#加入到词语列表中
        for index in word_list:#遍历词语列表
            if index in word_dict:
                word_dict[index]+=1#根据字典键访问键值，如果该键在字典中，则其值+1
            else:
                word_dict[index]=1#如果键不在字典中，则设置其键值为1

        #word_list = sorted(word_dict.items(),key=lambda e:e[1],reverse=True) # 排序
        return word_list
a= ['春','夏','秋','冬','春天','夏天','秋天','冬天','春','夏','秋','冬','春天','夏天','秋天','冬天','现在','我们']
season_ci =['春','夏','秋','冬','春天','夏天','秋天','冬天']
city = ['北京','上海','广州' ,'成都','重庆','南京' ,'苏州','杭州','青岛','合肥','济南' ,'武汉','郑州','厦门','拉萨','杭州','长沙','三亚','昆明','西安','香港','台湾','澳门']
# a =word_list('zonghe.txt')
#print(type(word_list('zonghe.txt')))
r_dict ={}
for x in a :
    if x in season_ci:
        if x=='春' or x=='春天' or x=='春天里':
                r_dict['春天'] = 1
        else:
            r_dict['春天'] += 1
print(r_dict)
# b = Counter(a)
# print(b)