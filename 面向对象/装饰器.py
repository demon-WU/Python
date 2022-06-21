class Student:
    __name='wutaixin'
    __age='18'
    __adress='广东省茂名市'
    @property   #装饰器定义一个函数getter
    def name(self):
        return self.__name
    @name.setter    #装饰器定义一个函数setter
    def name(self,name):
        self.__name=name
        pass
    pass
s=Student()
print(s.name)
s.name='linshuying'
print(s.name)