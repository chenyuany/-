#-*- coding:utf-8 -*-
#__author__ = 'chenyuanyuan'
from selenium import webdriver
import os,time
driver=webdriver.Chrome()
driver.get("https://172.16.10.195")
#输入用户名称
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("a")
#输入密码
driver.find_element_by_id("pwd").clear()
driver.find_element_by_id("pwd").send_keys("1")
time.sleep(3)
#点击登录按钮
driver.find_element_by_id("do_login").click()
#打印title
tile=driver.title
print(tile)
driver.switch_to_frame("content1")
driver.switch_to_frame("topFrame")
time.sleep(1)
driver.find_element_by_link_text("系统配置").click()
time.sleep(1)
driver.find_element_by_link_text("集中管理").click()
time.sleep(2)
driver.switch_to.parent_frame()
driver.switch_to_frame("mainFrame")
time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[1]/div/div/input[2]").click()
driver.find_element_by_id("btn_sc").click()
print("上传成功")