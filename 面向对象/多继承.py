class A:
    def eat(self):
        print("A方法")
        pass
    pass
class C:
    def eat(self):
        print('多继承')
    pass
class B(A,C):
    def eat(self):
        print("B方法")
        pass
    pass

b=B()
b.eat()
#C先找自身,自身没有再找继承的父类A-->B,找到为止
