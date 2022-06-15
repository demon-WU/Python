# class People:
#     def eat(self):
#         '''
#         吃的行为
#         :return:
#         '''
#         print('我喜欢吃榴莲')
#         pass
#     pass
# XM=People()
# XM.eat()
# XM.name='小明'    #添加实例属性
# XM.age=18

# class People:
#     name='wtx'
#     age=18
#     sex='man'
#     def __init__(self):
#         self.name='lsy'     #类似于java中的构造方法
#     def Run(self):
#         print('快爬')
#         pass
#     pass
#
# wtx=People()    #创建对象时自动执行_init_方法
# print(wtx.name)
# print(wtx.age)
# print(wtx.sex)

class People:
    def __init__(self,name,age,city,sex):
        self.name=name      #类似于java中的构造方法
        self.age=age
        self.city=city
        self.sex=sex
    def Run(self):
        print('快爬')
        pass
    pass

wtx=People('wtx',18,'maoming','nan')    #创建对象时自动执行_init_方法
print(wtx.name)
print(wtx.age)
print(wtx.sex)