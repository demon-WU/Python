class Person(object):
    __name='wutaixin'
    __age=18
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
        pass
    def __str__(self):
        return '姓名为{}，年龄为{}'.format(self.__name,self.__age)
    @property
    def name(self):
        return 'name:{}'.format(self.__name)
    @name.setter
    def name(self,name):
        self.__name=name
        pass
    @property
    def age(self):
        return 'age:{}'.format(self.__age)
    pass
    @age.setter
    def age(self,age):
        try:
            if 0<age<120:
                self.__age=age
        except Exception as msg:
            print('msg')
        else:
            print('输入年龄合法')
            pass
        finally:
            print('修改age结束')
            pass
        pass
    pass
p=Person('linshuying',18)
print(p.name)
print(p.age)
p.name='wtx'
p.age=19
print(p)
print(p.age)
print(p.name)



