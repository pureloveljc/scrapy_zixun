__author__ = "purelove"
__date__ = "2018/2/16 下午9:43"

# 枚举  绿钻 黄钻 红钻 黑钻

# from enum import Enum
#
#
# class VIP(Enum):
#     YELLOW = 1
#     green = 2
#     black = 3
#     red = 4
#
#
# print(VIP.YELLOW.name)

# 枚举是一个类  和普通类有什么区别 枚举不能被更改 .name 名字 .value值
#
# list_x=[1,2,3,4]
# print(list(map(lambda x:x*x,list_x)))

# f= lambda x,y:x+y #匿名函数
# print(f(1,2))

#三元表达式 真 if 条件判断 else 假


# 对那些项目经验不足的新人，适当的增加基础技术比例，
# 比如    - 谈谈装饰器，迭代器，yield，内存管理等    - Python高并发解决方案
# - 计算密集型，IO密集型任务怎么办    - Tcp/Udp协议，Http协议    -
# sql，cache, nosql    - web安全相关，sql注入，xss等
#
#from study_two import Person


# class Student():
#     name = "1111"
#     age =""
#     sum = 0
# # 子类方法 调用父类的方法
#     def __init__(self,name,age,shengao,xueliang):
#         self.name = name
#         self.age = age
#         self.shengao =shengao
#         self.__class__.sum+=1#访问类变量
#         #super(Student, self).__init__(xueliang)
#         #Person.__init__(self,xueliang)
#         print(self.name)
#         print(self.age)
#         print(self.shengao)
#         print("当前学生的总数:"+str((self.__class__.sum)))
#         url ="www.baidu.com"
#
#
#     def print_home(self):
#         #super(Student, self).print_home()
#         print("doing home")
#
#     def __marking(self,score):
#         if score<0:
#             print("不能打负分")
#             self.__score = 0
#         else:
#             #score=0
#             self.__score = score
#         print(self.name+"的分数为:"+str(self.__score))
#
#
#     @classmethod
#     def eating(cls):
#         cls.sum += 1 #注意和实例方法的区别  是不是类方法 主要看 @classmethod
#         #  实例方法和类方法的区别
#
#
# purelove=Student('ljc',18,170,"300xue")
#purelove2 = Student('pure',19,260)
#purelove._Student__marking(-1)
#print(purelove.score)
#print(purelove.score)
#print(purelove.name)
#print(purelove.)
#print(Student.name)
#print(purelove.__dict__)#dict里面保存着 对象下面所有的变量