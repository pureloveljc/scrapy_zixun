# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = '2018/5/3 13:18'
import jieba
#  cinpin计算和wordcloud用的python版本不一样。
#读词
file=open("E:\ljcprojects\music_fenxi\\all_songs\song_liuxing\zonghe.txt",'r',encoding="utf8")
lyric_str=file.read()
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

word_list = sorted(word_dict.items(),key=lambda e:e[1],reverse=True) #排序

print(word_list)
print(len(word_list))

fcc=open("E:\ljcprojects\music_fenxi\\fenxi_result\liuxing\\fenci_top100.txt",'w')

for x in word_list[0:101]:
    fcc.write(x[0]+str(x[1])+'\n')
fcc.close()

# 生成图表
from pyecharts import Bar
top_100 = word_list[0:51]
bar = Bar("流行音乐", "出现频率最高的词")
ci_list = []
num_list = []
for x in top_100:
    ci_list.append(x[0])
    num_list.append(x[1])
print(ci_list)
print(num_list)
bar.add("Top50", ci_list, num_list,is_more_utils=True,weight =1800,height =800)
bar.show_config()
bar.render()
