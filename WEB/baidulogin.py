#--coding:utf-8--
#__author__ = 'chenyuanyuan'
from selenium import  webdriver
driver=webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.find_element_by_link_text(u"登录").click()
driver.find_element_by_id("TANGRAM__PSP_8__userName").clear()
driver.find_element_by_id("TANGRAM__PSP_8__userName").send_keys("18500809752")
driver.find_element_by_id("TANGRAM__PSP_8__password").clear()
driver.find_element_by_id("TANGRAM__PSP_8__password").send_keys("1")
driver.find_element_by_id("TANGRAM__PSP_8__submit").click()

