__author__ = "purelove"
__date__ = "2018/2/24 下午1:20"
import time
from functools import wraps
# 装饰器
# 可以接受定义的时候的复杂 ，不可以接受调用时候的复杂
def decorator(func):
    #print("1 ")
    @wraps(func) #保证原有的参数不变
    def wraaper(*args,**kw):
        print(time.time())
        #print("2")
        func(*args,**kw)
        # def print_a():
        #     print("第三个功能")
        # print_a()
    return wraaper


@decorator
def f1(a):
    print("3"+a)

@decorator
def f2(b,c,d):
    print(b,c,d)

@decorator
def f3(func1,func2,**kw):
    print("第一个参数"+func1,"第二个参数"+func2,kw)

#f1('56')
#f2('2','3','4')
f3('a','b',北京="36c")
#decorator(f1)
# 调用f1() aop设计思维