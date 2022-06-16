class Dog:
    def __init__(self,name,color):
        self.name=name
        self.color=color
        pass
    def sound(self):
        print('汪汪叫……')

class keji(Dog):
    def __init__(self,name,color):
        super(keji, self).__init__(name,color)
        #使用这个方法之后就可以使用父类的name和color实例属性了
        #self.name=name
        #self.color=color
        self.hight=30
        self.weight=40
        pass
    def __str__(self):
        return '{}的身高是{}颜色是{}体重是{}'.format(self.name,self.hight,self.color,self.weight)
    def sound(self):
        print('嘻嘻叫……')
        print(self.name)
        pass
    pass
KEji=keji('柯基','黄色')
KEji.sound()
print(KEji)