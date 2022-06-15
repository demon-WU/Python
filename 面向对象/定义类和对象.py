class Person:
    name='wtx'
    age=18
    city='maoming'
    def eat(self):
        print('再吃东西就没钱了')
        pass
    def run(self):#实例方法
        self.name='小花'#实例属性，类似于局部变量
        print('{}跑快点'.format(self.name))
        pass
    pass
go=Person()
print(go.name)
go.eat()
go.run()

