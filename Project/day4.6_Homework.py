def funcation_A(*args):
    '''
    接收n个数字，求这些参数数字的和
    :param args:
    :return:
    '''
    sum=0
    for i in args:
        sum+=i
    return sum
# print(funcation_A(1,2,3,4,5,6))

def funcation_B(con):
    '''
    找出传入的列表或元组的奇数位对应的元素，并返回一个新的列表
    :param con:
    :return:
    '''
    A=[]
    index=1
    for i in con:
        if index%2==1:
            A.append(i)
        index+=1
    return A
# B=[1,2,3,4,5]
# print(funcation_B(B))
def funcation_C(dict):
    newDict={}
    for key,value in dict.items():
        if len(value)>2:
            newDict[key]=value[:2]
        else:
            newDict[key]=value
    return newDict
print(funcation_C({'name':'吴泰鑫','age':'39','city':'茂名市'}))

