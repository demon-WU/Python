class School:
    __student='吴泰鑫'
    __id='1001'
    __age=18
    __adress='广东省茂名市'
    #定义私有属性格式:__name
    @classmethod
    def getStudentid(cls):
        '''
        返回ID
        :return:
        '''
        return School.__id

    pass
s=School()
print(s.getStudentid())