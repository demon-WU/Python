import random
i=3
age =random.randint(1,100)
print(age)
while i>=0:
    if i!=0:
        guess= int(input("我猜是："))
        if guess==age:
            print("你猜对了，年龄为%d"%age)
            break
        else:
            if guess<age:
                print("猜小了，再来")
            else:
                print("猜大了，再来")
            i-=1
    elif i==0:
        answer=input('是否打算继续玩？Y、y/N、n')
        if answer=='y' or answer=='Y':
            i=3
        elif answer=='N' or answer=='n':
                print("游戏结束")
                break