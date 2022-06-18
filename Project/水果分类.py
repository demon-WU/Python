class Fruits:
    def say_what(self):
        '''
       这个水果是神恶魔
       :return:
       '''
        print('这是水果')
        pass

    pass


class Origin(Fruits):
    def say_what(self):
        '''
        这是一只橙子
        :return:
        '''
        print('这是一只橙子')
        pass

    pass


class Apple(Fruits):
    def say_what(self):
        '''
        分类
        :return:
        '''
        print('这是一个苹果')
        pass

    pass


apple = Apple()
apple.say_what()
origin=Origin()
origin.say_what()
