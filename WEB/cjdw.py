#--coding:utf-8--
#__author__ = 'chenyuanyuan'
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
driver=webdriver.Firefox()
file_path='file:///'+os.path.abspath("b.html")
driver.get(file_path)

driver.refresh()
time.sleep(2)
driver.find_element_by_link_text("Link1").click()
driver.delete_all_cookies()
menu=driver.find_element_by_id("dropdown1").find_element_by_link_text("Another action")
#鼠标移动到元素上
ActionChains(driver).move_to_element(menu).perform()
driver.quit()