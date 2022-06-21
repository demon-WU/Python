a=[20,21,32]
try:
    print(a[10])
    pass
except IndexError as msg:
    '''
    抛出异常
    '''
    print(msg)
    pass
except NameError as msg:
    '''
    抛出异常
    '''
    print(msg)
    pass
print('执行抛异常成功')