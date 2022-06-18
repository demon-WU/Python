class fish:
    def __speakName(self):
        #__speakName私有化方法，无法实例化调用方法或被继承
        '''
        描述名字
        :return:
        '''
        print('鲫鱼')
        pass
    pass
fishers=fish()
class ff(fish):
    pass
#继承也无法使用私有化方法