class LongLengString(Exception):
    #继承异常处理基类
    '''
    自定义抛出异常
    '''
    def __init__(self,len):
        '''
        编写抛出异常传参
        :param len:
        '''
        self.len=len
    def __str__(self):
        '''
        异常返回结果信息
        :return:
        '''
        return '您输入的姓名过长:'+str(self.len)+";请重新输入"
    pass

def s():
    try:
        name = input('请输入姓名')
        if len(name)>5:
            raise LongLengString(len(name))
            #抛出异常前需传参进入抛异常类
        pass
    except LongLengString as msg:
        print(msg)
        pass
    else:
        print('代码正确')
        pass
    finally:
        print('程序结束')
        pass
    pass
s()

