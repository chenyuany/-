#-*- coding:utf-8 -*-
#__author__ = 'chenyuanyuan'
from  selenium import webdriver
import os,time
driver=webdriver.Firefox()
fil_path="file:///"+os.path.abspath("d.html")
driver.get(fil_path)
driver.find_element_by_id("ShippingMethod").click()
driver.find_element_by_xpath(".//*[@id='ShippingMethod']/option[3]").click()
time.sleep(3)
driver.quit()