class People:
    def __init__(self,name,age,city,sex):
        self.name=name      #类似于java中的构造方法
        self.age=age
        self.city=city
        self.sex=sex
        print('init------------------>执行')
        pass

    def Run(self):
        print('快爬')
        pass
    pass
    def __new__(cls, *args, **kwargs):  #先执行这个函数
        '''
        每调用一次生成一个新对象
        :param args:
        :param kwargs:
        '''
        print('new--------->执行')
        return object.__new__(cls)  #在此处才是创建对象实例的位置 必须要这一步返回实例，否则对象创建不成功
wtx=People('wtx',18,'maoming','nan')    #创建对象时自动执行_init_方法
