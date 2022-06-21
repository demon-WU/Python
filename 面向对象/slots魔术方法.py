#作用：限制添加的属性
class Student:
    __slots__ = ('name','age','pro')
    #---->一个元组序列
    #字符串类型，限制动态绑定属性
    def __str__(self):
        return '{}----------{}'.format(self.name,self.age)
    pass
pass
s=Student()
s.name='wtx'
s.age=18
s.pro='物理'  #没有在范围内不能添加
print(s.__dict__)
#所有可以用的属性都在这里存储 不足的地方就是占用的内存空间大
#当使用了__slots__魔术方法后实例中不再存在__dict__魔术方法