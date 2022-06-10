import random
# 0:拳头 1:剪刀 2:布
putHand = int(input("请出拳:"))
if putHand < 0 or putHand > 2:
    print('输入非法字符，请重新输入')
    pass
computerHand = random.randint(0,2)
if putHand == computerHand:
    print("平局")
elif putHand ==0 and computerHand ==1:
    print('你赢了')
elif putHand == 1 and computerHand == 2:
    print('你赢了')
elif putHand == 2 and computerHand == 0:
    print('你赢了')
else:
    print('你输了')
print(computerHand)