import time
class Animal:
    def __init__(self,name):
        self.name=name
        print('构造函数')
        time.sleep(1)
        pass
    def __str__(self):
        return '这是一只%s'%self.name
        pass
    def __del__(self):
        '''
        最后执行，自动执行
        这个对象被彻底清理掉。内存控件也被释放了
        :return:
        '''
        print('析构方法正在进行')
        pass
    pass

cat=Animal('猫')
print(cat)

