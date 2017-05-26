#--coding:utf-8--
#__author__ = 'chenyuanyuan'
from  selenium import  webdriver
driver=webdriver.Firefox()
driver.get("https://www.baidu.com")
# #获取现在窗口
# first_url=driver.current_window_handle
# driver.find_element_by_link_text("登录").click()
# driver.find_element_by_link_text("立即注册").click()
# #获取所有窗口
# allwindows=driver.window_handles
# for window in allwindows:
# 	if window != first_url:
# 		driver.switch_to_window(window)
# 		print(u"现在是注册窗口")
# 		driver.close()
# driver.switch_to_window(first_url)
# driver.find_element_by_id("kw").send_keys(u"注册成功")

