# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = '2018/5/3 19:40'

import jieba
from scipy.misc import imread  # 这是一个处理图像的函数
from wordcloud import WordCloud
from wordcloud import STOPWORDS
from wordcloud import ImageColorGenerator
import matplotlib.pyplot as plt
import os
from pyecharts import Bar,Pie,Line

back_color = imread('E:\ljcprojects\music_fenxi\img\yueyu.jpg')  # 解析该图片

wc = WordCloud(background_color='white',  # 背景颜色
               max_words=1000,  # 最大词数
               mask=back_color,  # 以该参数值作图绘制词云，这个参数不为空时，width和height会被忽略
               max_font_size=100,  # 显示字体的最大值
               stopwords=STOPWORDS.add('the'),  # 使用内置的屏蔽词，再添加'苟利国'
               font_path="E:\ljcprojects\music_fenxi\\font\simhei.ttf",  # 解决显示口字型乱码问题，
               random_state=42,  # 为每个词返回一个PIL颜色
               width=2000, height=2000
                # width=100,  # 图片的宽
                # height=100  #图片的长

               )
# WordCloud各含义参数请点击 wordcloud参数

# 添加自己的词库分词，比如添加'金三胖'到jieba词库后，当你处理的文本中含有金三胖这个词，
# 就会直接将'金三胖'当作一个词，而不会得到'金三'或'三胖'这样的词
#jieba.add_word('金三胖')

# 打开词源的文本文件
text = open('E:\ljcprojects\music_fenxi\\all_songs\song_yueyu\zonghe.txt').read()


# 该函数的作用就是把屏蔽词去掉，使用这个函数就不用在WordCloud参数中添加stopwords参数了
# 把你需要屏蔽的词全部放入一个stopwords文本文件里即可
def stop_words(texts):
    words_list = []
    word_generator = jieba.cut(texts, cut_all=False)  # 返回的是一个迭代器
    with open('stopwords.txt') as f:
        str_text = f.read()
        unicode_text = unicode(str_text, 'utf-8')  # 把str格式转成unicode格式
        f.close()  # stopwords文本中词的格式是'一词一行'
    for word in word_generator:
        if word.strip() not in unicode_text:
            words_list.append(word)
    return ' '.join(words_list)  # 注意是空格


text = stop_words(text)
print(text)

wc.generate(text)
# 基于彩色图像生成相应彩色
image_colors = ImageColorGenerator(back_color)
# 显示图片
plt.imshow(wc)
# 关闭坐标轴
plt.axis('off')
# 绘制词云
plt.figure()
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis('off')
# 保存图片
wc.to_file('E:\ljcprojects\music_fenxi\\yueyu.png')


# 生成图表
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
#
# from pyecharts import Bar
# bar = Bar("流行音乐", "出现频率最高的词")
# bar.add("Top50", ["一个", "自己", "世界", "什么", "爱情", "不要"], [549, 540, 481, 376, 364, 350],is_more_utils=True)
# bar.show_config()
# bar.render()


