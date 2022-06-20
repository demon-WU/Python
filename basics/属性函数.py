class Student:
    __name='小明'
    __age='18'
    __address='广东省'
    '''
    私有属性
    '''
    def set_name(self,name):
        self.__name=name
        pass
    def get_name(self):
        return self.__name
    def set_age(self,age):
        self.__age=age
        pass
    def get_age(self):
        return self.__age
    def set_address(self,address):
        self.__address=address
        pass
    def get_address(self):
        return self.__address
    name=property(get_name,set_name)
    age=property(get_age,set_age)
    address=property(get_address,set_address)
s=Student()
print(s.name)
s.name='小红'
print(s.name)
print(s.age)
s.age='19'
print(s.age)
print(s.address)
s.address='广东省茂名市'
print(s.address)

