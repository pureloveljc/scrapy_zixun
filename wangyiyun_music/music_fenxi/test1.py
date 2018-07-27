# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = '2018/5/3 19:40'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from pyecharts import Pie

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [100, 12, 13, 10, 10, 10]
pie = Pie("饼图示例")
pie.add("", attr, v1, is_label_show=True)
pie.show_config()
pie.render()