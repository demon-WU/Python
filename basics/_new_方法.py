#__new__函数多用于设计单例模式
class Student:
    _instance=None
    # def __init__(self,name,age):
    #     print(age,name)
    #     pass
    def __new__(cls, *args, **kwargs):
        '''
        只创建一个对象
        :param args:
        :param kwargs:
        '''
        if not cls._instance:
            cls._instance=super(Student,cls).__new__(cls)
            return cls._instance
        else:
            return cls._instance
        pass
    pass
s=Student()
print(id(s)) #地址均为相同
s1=Student()
print(id(s1))   #地址均为相同

