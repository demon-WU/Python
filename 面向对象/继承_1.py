class Animual:
    def animual_sound(self,name):
        self.name=name
        print("{}的叫声是这样的".format(self.name))
        pass
    def animual_way(self,name):
        self.name=name
        print('%s都是喜欢乱动的'%self.name)
        pass

    pass
class Cat(Animual):
    def Eat(self,name):
        self.name=name
        print('{}都喜欢吃猫粮'.format(self.name))
        pass
    pass
class Dog(Animual):
    def Eat(self,name):
        self.name=name
        print('{}都喜欢吃狗粮'.format(self.name))
        pass
    pass
cat=Cat()
cat.Eat('猫猫')
cat.animual_sound('猫猫')
cat.animual_way('猫猫')
dog=Dog()
dog.Eat('狗狗')
dog.animual_sound('狗狗')
dog.animual_way('狗狗')