#-*- coding:utf-8 -*-
#__author__ = 'chenyuanyuan'
from  selenium import  webdriver
import time
driver=webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.find_element_by_link_text("设置").click()
driver.find_element_by_link_text("搜索设置").click()
# driver.find_element_by_class_name("setpref").click()
driver.find_element_by_class_name("prefpanelgo").click()
#获取网页警告信息
alert=driver.switch_to_alert()
# as1=alert.text
# print(as1)
# alert.accept()
# time.sleep(3)
alert.dismiss()
driver.quit()
