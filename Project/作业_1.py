# 求三组连续自然数的和：求1到10、20到30和35到45的三个和
a=sum(range(1,11))
print(a)

b=sum(range(20,31))
print(b)

c=sum(range(35,46))
print(c)
# # 100个和尚吃100个馒头，大和尚一人吃3个馒头。小和尚三人吃一个馒头。请问大小和尚各多少人？
def PersonCount():
    '''
    100个和尚，设大和尚a个，小和尚为100-a
    :return:
    '''
    for a in range(100):
        if a*3+(100-a)*(1/3)==100:
            return (a,100-a)
print(PersonCount())
# 指定一个列表，列表里含有唯一一个只出现过一次的数字，写程序找出者‘独一无二’的数字
def numberChoose(List):
    l=[]
    set1=set(List)
    for i in set1:
        List.remove(i)
        pass
    set2=set(List)
    for i in set1:
        if i not in set2:
            l.append(i)
            pass
        pass
    return l
    pass
A=[1,1,2,2,3,4,5,6,6,7]
print(numberChoose(A))
