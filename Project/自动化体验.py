from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
fine_id=driver.find_element(By.ID,'kw')