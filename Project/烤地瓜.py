#烤地瓜项目
#地瓜该有的属性有:状态、时间、调味料
class SweetTotato():
    #初始化实例属性
    def __init__(self):
        #烤的时间
        self.Time = 0
        # 地瓜状态
        self.State = '生'
        #调味料添加记录
        self.Seasoner = []
        pass
    def __str__(self):
        return "烤了{}分钟,地瓜{}，添加了{}调料".format(self.Time,self.State,self.Seasoner)
    #烤地瓜的动作方法
    def Barbecue(self,time):
        # 时间累加
        self.Time+=time
        if self.Time < 3:
            self.State = '一成熟'
            pass
        elif 10 >= self.Time >= 3:
            self.State = '三成熟'
            pass
        elif 20 >= self.Time > 10:
            self.State = '八成熟'
            pass
        elif 30 >= self.Time > 20:
            self.State = '全熟了'
            pass
        elif self.Time > 30:
            self.State = '糊了'
            pass
        pass
    #添加调料函数
    def Add(self,seasoner):
        self.Seasoner.append(seasoner)
        pass
    pass
st = SweetTotato()
st.Barbecue(10+20)
st.Add('辣椒面')
print(st)