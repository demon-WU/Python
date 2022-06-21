class Student:
    __slots__ = ('name','age','pro')
    #---->一个元组序列
    #字符串类型，限制动态绑定属性
    def __str__(self):
        return '{}----------{}'.format(self.name,self.age)
    pass
pass
class subStudent(Student):
    __slots__ = ('gender')
    def __str__(self):
        return '{}'.format(self.gender)
    pass
s=subStudent()
s.gender='小儿麻痹症'
print(s)