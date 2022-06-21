import types
def ChangeMethog(self):
    #动态增加实例方法
    print('{}的年龄为{}，专业为{}'.format(self.name,self.age,Student.pro))
    pass
@classmethod
def classTest(cls):
    print('这是动态绑定类方法')
    pass
class Student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        pass
    def __str__(self):
        return '{}的年龄为{}'.format(self.name,self.age)
    pass
Student.test=classTest
#动态绑定类方法
s=Student('wtx',18)
s.test()







# xm=Student('小明',18)
# print(xm)
# Student.pro='物理'
# print(xm.pro)
# xm.inputDef=types.MethodType(ChangeMethog,xm)
# # 动态绑定实例方法
# xm.inputDef()