class People:
    def __init__(self,name,age,city,sex):
        self.name=name      #类似于java中的构造方法
        self.age=age
        self.city=city
        self.sex=sex
    def __str__(self):
        return "%s 是%s的，住在%s，今年%d"%(self.name,self.sex,self.city,self.age)
    def Run(self):
        print('快爬')
        pass
    pass

wtx=People('wtx',18,'maoming','nan')    #创建对象时自动执行_init_方法
print(wtx)  #_str_魔术方法可以直接打印对象
print(wtx.name)
print(wtx.age)
print(wtx.sex)