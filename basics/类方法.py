class WorldCountry:
    country='China'
    @classmethod
    def getConutry(cls):
        '''
        查看类属性country的值
        :return:
        '''
        return cls.country
    pass
    @classmethod
    def setCountry(cls,country):
        '''
        修改创建类属性country的值
        :return:
        '''
        cls.country=country
        return cls.country
    pass
c=WorldCountry()
print(c.country)
c.setCountry('英国')
print(WorldCountry.country)
