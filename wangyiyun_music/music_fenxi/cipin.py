# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = '2018/5/3 13:18'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import jieba

#读词
file  =  open("/Users/purelove/LjcSpider/music_fenxi/all_songs/song_liuxing/zonghe.txt",'r')
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

word_list = sorted(word_dict.items(),key=lambda e:e[1],reverse=True) #排序

print(word_list)
print(len(word_list))

fcc = open("/Users/purelove/LjcSpider/music_fenxi.txt",'w')

for x in word_list[0:101]:   #提取前20个高频词  这边可以配置
    fcc.write(x[0]+str(x[1])+'\n')
fcc.close()

top_100 = word_list[0:11]
ci_list = []
num_list = []
for x in top_100:
    ci_list.append(x[0])
    num_list.append(x[1])
# 生成图表  柱状图   pyecharts配置很丰富 可以依据数据生成自己喜欢的图表，包括颜色等。 很棒的一个数据可视化工具
from pyecharts import Bar
bar = Bar("流行音乐", "出现频率最高的词")
print(ci_list)
print(num_list)
bar.add("Top30", ci_list, num_list,is_more_utils=True,weight =1800,height =800)
bar.show_config()
bar.render()

# 生成图表  大饼图
# from pyecharts import Pie
#
# attr = ci_list
# v1 = num_list
# pie = Pie("")
# pie.add("", attr, v1, is_label_show=True)
# pie.show_config()
# pie.render()


