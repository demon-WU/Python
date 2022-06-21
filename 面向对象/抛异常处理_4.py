def a(s):
    return 10/int(s)
    pass
def b(s):
    return a(s)*2
def main():
    '''
    主函数中抛出异常即可
    :return:
    '''
    try:
        # b('0')
        print('正常运行')
        pass
    except Exception as msg:
        print(msg)
        pass
    else:
        print('代码块没抛异常时执行')
        pass
    finally:
        print('不管有没有异常都需要处理')   #主要用于释放资源----数据库连接占用的资源等
        pass
    pass
main()