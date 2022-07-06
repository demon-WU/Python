# import time
# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get('https://www.baidu.com/')
# a=driver.find_element(By.ID,'kw')
# a.send_keys('寄你太美')
# time.sleep(2)
# b=driver.find_element(By.ID,'form')
# b.click()
# b=driver.find_element(By.ID,'su')
# b.click()

class Wash():
    def funcation(self):
        print('可以洗衣机')
        #获取实例属性
        print("宽度为{},高度为{}".format(self.width,self.height))
        pass
    pass
haier=Wash()
# 实例属性
haier.height=500
haier.width=800

haier.funcation()