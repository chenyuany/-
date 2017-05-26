#--coding:utf-8--
#__author__ = 'chenyuanyuan'
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
driver=webdriver.Firefox()
file_path='file:///'+os.path.abspath("a.html")
driver.get(file_path)
driver.switch_to_frame("f1")
driver.switch_to_frame("f2")
driver.find_element_by_id("kw").send_keys("yuanyuan")
driver.find_element_by_id("su").click()