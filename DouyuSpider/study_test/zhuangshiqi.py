__author__ = "purelove"
__date__ = "2018/2/24 下午12:58"

#装饰器 如果有100个函数，每一个函数都要打印时间戳
# 修改是封闭的，扩展是开发的
# 为了 解决这个问题 专门编写一个函数
# 装饰器 新添加的业务逻辑 功能的增加  但是不改变函数本身的逻辑
import time

def f1():
    #print(time.time()) #时间戳
    print("this is a  one function")


def f2():
    #print(time.time()) #时间戳
    print("this is a two function")

def print_current_time(func,func1,*func3):
    print(time.time())
    func()
    print(time.time())
    func1()
    print_current_time()
    func3()


print_current_time(f1,f2)
#print_current_time(f2)