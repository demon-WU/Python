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
        b('0')
        pass
    except Exception as msg:
        print(msg)
        pass
    pass
main()
