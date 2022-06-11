
import math
import random

g=10 #重力加速度
m=0.026 #一根箭的重量
air_friction=random.random()  #生成随机0-1的小数
intX=1.2 #靶心到地面的高度
intS=10 #靶子与人的距离
# 平抛运动：垂直距离h=1/2gt**2 水平运动:s=vt
# 力与速度的计算公式:F=ma
# 存在水平的空气阻力影响 air_friction
def time(h,g=10):
    '''
    计算射手从高处下落到靶心距离的高度
    :param h:
    :return:
    '''
    t=math.sqrt(2*h/g)
    return h

def shoot(F,m=0.026):
    '''
    射箭的速度
    :param F:
    :return:
    '''
    v=F/m
    return v
i = 10
#射十次箭
while i>0:
    F = float(input("我要蓄力了:"))
    #射箭使用的力
    F1=F-air_friction
    #实际可用的力
    h=float(input('我在这个角度射箭:'))
    h1=h-intX
    #射箭用的高度
    t=time(h1)
    v=shoot(F1)
    if v*t-intS<0 and h1>0.2:
        print('脱靶了')
    elif v*t==intS and h1==intX:
        print("命中靶心了，你真棒")
    else:
        print("没中，真可惜，再来")
    i-=1


