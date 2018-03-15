__author__ = "purelove"
__date__ = "2018/2/14 下午3:43"
import re

#line = "peeeeeeelplove123"

#regex_str= ".*?(p.*?l).*"
# ^ 以什么什么开始  $ 以什么什么结尾 ?#非贪婪匹配
# + 至少一次 {2}限定前面的字符出现2次  {2,}2次以上  {2,5}2到5次
# 限定词都是 放在 字符的前面  b{2}
# | 或  （a|b）a或b
# [abcde] 这里面的任意一个
# \s 匹配空格  \S只要不为空格
# \w 任意字符包括[a-zA-Z0-9_]         \W 相反
# 汉子[\u4e00-\u9fa5] \d 数字

# 保存的时候是utf-8 节省空间  读取的时候 unicode 内存里
# encode("utf-8") 编码 decode解码
# S="中文"
# S.decode("utf8").encode("utf8")
# match = re.match(regex_str,line)
#
#
# if re.match(regex_str,line):
#     print(match.group(1))