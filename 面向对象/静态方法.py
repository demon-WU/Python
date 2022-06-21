import time


class TimeCheck:
    hour=1
    minutie=30
    second=59
    def __init__(self,hour,minutie,second):
        self.hour=hour
        self.minutie=minutie
        self.second=second
    @staticmethod
    def getTime():
        '''
        静态获取时间
        :return:
        '''
        return time.strftime('现在北京时间为:%H:%M:%S',time.localtime())
    pass
s=TimeCheck(10,20,30)
print(TimeCheck.getTime())  #该方法区别在于静态方法是独立的，不受类对象、实例对象等影响