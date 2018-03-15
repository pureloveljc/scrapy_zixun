__author__ = "purelove"
__date__ = "2018/2/24 下午1:58"

#装饰器 语法糖  @

# list_x =[1,2,3,4,5]
# list_y =[2,3,4,5,6]
#
# r= map(lambda x,y:x*x+y,list_x,list_y)
#
# print(list(r))


# reduce 连续

from functools import reduce

# a = reduce(lambda x,y:x+y,list_x) #（1+2）+3）+4）+5）
#
# print(a)


#(0,0)

# init= [(1,3),(2,-2),(-2,3)]
#
# a=reduce(lambda a,b:[a[0]+b[0],a[1]+b[1]],init)
# print(a)
# 记录

# coordinate = [[1, 6], [2, 7], [-1, -3]]
#
#
# # 二
# result = reduce(lambda x, y: [x[0] + y[0], x[1] + y[1]], coordinate)
# print(result)

try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print ("Error: 没有找到文件或读取文件失败")
else:
    print ("内容写入文件成功")
    fh.close()