# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = '2018/5/4 11:10'
# encoding: utf-8
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from pyecharts import Bar
bar = Bar("流行音乐", "出现频率最高的词")
bar.add("Top50", ["一个", "自己", "世界", "什么", "爱情", "不要"], [549, 540, 481, 376, 364, 350],is_more_utils=True)
bar.show_config()
bar.render()
