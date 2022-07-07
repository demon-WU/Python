# 搬家具小项目
class House():
    def __init__(self,space):
        #房子地理位置
        self.location = '茂名'
        # 房子总面积
        self.space = space
        # 房子剩余面积
        self.outSpace = self.space
        #家具列表
        self.furnitur = []
        pass
    def __str__(self):
        return '房子坐落{}，总面积为{}，现有家具{},房子剩余面积为{}'.format(self.location,self.space,self.furnitur,self.outSpace)
    def moveIn(self,f):
        if self.outSpace <= f.paySpace:
            print('剩余房子面积为{},搬不进去了'.format(self.outSpace))
            pass
        else:
            self.outSpace -= f.paySpace
            self.furnitur.append(f.name)
        pass
    def moveOut(self,f):
        self.furnitur.remove(f.name)
        self.outSpace += f.paySpace
        pass
    pass

class Furnnitur():
    def __init__(self,name,paySpace):
        #家具名称
        self.name = name
        #占地面积
        self.paySpace = paySpace
        self.dict = {self.name:self.paySpace}
        pass
    def __str__(self):
        return '家具:{}，大小:{}'.format(self.name,self.paySpace)
    pass



wtx = House(100)
a = Furnnitur('沙发',10)
print(wtx)
print(a)
wtx.moveIn(a)
print(wtx)
wtx.moveOut(a)
print(wtx)
