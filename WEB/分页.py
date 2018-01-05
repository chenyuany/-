#-*- coding:utf-8 -*-
#__author__ = 'chenyuanyuan'
from  selenium import webdriver
import time,os
from selenium.webdriver.common.keys import Keys
driver=webdriver.Firefox()
fil_path="file:///"+os.path.abspath("e.html")
driver.get(fil_path)
total_pages=len(driver.find_element_by_tag_name("select").find_elements_by_tag_name("option"))
print ("total page is %s" %(total_pages))
time.sleep(3)
pages=driver.find_element_by_tag_name("select").find_elements_by_tag_name("option")
#再次获取所分页，并执行循环翻页操作
for page in pages:
	page.click()
	time.sleep(2)
time.sleep(3)
driver.quit()



# driver.get("https://172.16.10.183")
# driver.find_element_by_id("username").clear()
# driver.find_element_by_id("username").send_keys("a")
# driver.find_element_by_id("pwd").clear()
# driver.find_element_by_id("pwd").send_keys("1")
# #driver.find_element_by_id("do_login").click()
# driver.find_element_by_id("do_login").send_keys(Keys.ENTER)
# time.sleep(3)
# #跳转到窗体
# driver.switch_to.frame("content1")
# driver.switch_to_frame("mainFrame")
# driver.switch_to_frame("rigthFrame")
# #获取所有分页的数量，并打印
# total=len(driver.find_element_by_tag_name("select").find_element_by_tag_name("option"))
# print ("total page is %s" %(total))
