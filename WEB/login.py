#--coding:utf-8--
#__author__ = 'chenyuanyuan'
#导入webdriver
from selenium import  webdriver
#引入ActionChains
from selenium.webdriver.common.action_chains import ActionChains
#引入keybao
from selenium.webdriver.common.keys import Keys
#引入webDriverWait
from selenium.webdriver.support.ui import  WebDriverWait
#导入time包
import time
import os

#调用火狐浏览器
driver=webdriver.Firefox()
driver.get("https://172.16.10.195")
#输入用户名称
driver.find_element_by_id("username").clear()
#webDriverWait使用
element=WebDriverWait(driver,10).until(lambda  driver: driver.find_element_by_id("username"))
element.send_keys("a")
#返回文字
te=driver.find_element_by_id("username").text
print(te)
#返回窗口大小
size=driver.find_element_by_id("username").size
print(size)
#返回属性值
ty=driver.find_element_by_id("username").get_attribute("type")
print(ty)
#判断该元素是否可见
disable=driver.find_element_by_id("username").is_displayed()
print(disable)
#输入密码
driver.find_element_by_id("pwd").clear()
driver.find_element_by_id("pwd").send_keys("1")
#添加智能等待
# driver.implicitly_wait(30)
#点击登录按钮
driver.find_element_by_id("do_login").click()
#打印title
tile=driver.title
print(tile)
if tile==u"LanSecS内控堡垒主机":
	print("登录成功")
else:
	print("登录失败")
#获取URL
now_url=driver.current_url
print(now_url)
if now_url =="https://172.16.10.195":
	print("url正确")
else:
	print("进入下一站")

#跳转到窗体
driver.switch_to.frame("content1")
driver.switch_to_frame("topFrame")
#获取登录的用户
now_user=driver.find_element_by_xpath("//*[@id='js_z']").text
print(now_user)
#添加固定休眠时间
time.sleep(5)
#进入用户页面
driver.find_element_by_xpath(".//*[@id='top_menu']/li[4]/p/a[2]").click()
time.sleep(2)
#勾选复选框
#方法一：
# #回到主窗口，重新定义窗口
# driver.switch_to_default_content()
# driver.switch_to_frame("content1")
# driver.switch_to_frame("mainFrame")
# #因为可能有重复的ID和xpath可能受frame的影响
# driver.find_element_by_css_selector("html body form#user_query div.container div#pagination div#blue_th.blue_th table.result tbody tr#title_tr th.no_lt span input#checkbox.checkbox").click()
#方法二
#回到父节点
driver.switch_to.parent_frame()
driver.switch_to_frame("mainFrame")
driver.find_element_by_css_selector("html body form#user_query div.container div#pagination div#blue_th.blue_th table.result tbody tr#title_tr th.no_lt span input#checkbox.checkbox").click()



















# print("最大化浏览器")
# driver.maximize_window()
#print("设置浏览器宽480，高800")
#driver.set_window_size(480,800)
#访问网页
# first_url="http://www.baidu.com"
# driver.get(first_url)
# # driver.find_element_by_id("kw").send_keys("selenium")
# # driver.find_element_by_id("su").click()
# second_url="https://172.16.10.196"
# driver.get(second_url)
# #返回
# driver.back()
# #前进
# driver.forward()
# name="yuanyuan"
# age=18
# print("my name is %s"%name)
# print("my age is %d"%age)
# #%s表示输出的类型为字符串，“%d”表示输出类型为整型数字，如果我们不确定变量类型的话可以使用%r
# print("my name is %s,age is %d"%(name,age))
#driver.quit()
# #右击元素
# yj=driver.find_element_by_xpath(".//*[@id='message']")
# ActionChains(driver).context_click(yj).perform()
# #双击元素
# ActionChains(driver).double_click(yj).perform()
# driver.get("http://www.baidu.com")
# driver.find_element_by_id("kw").send_keys("selenium")
# #删除多输入的m
# driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
# #输入空格键+“教程”
# driver.find_element_by_id("kw").send_keys(Keys.SPACE)
# driver.find_element_by_id("kw").send_keys(u"教程")
# #ctrl+a 全选输入框内容
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"a")
# #ctrl+x剪切
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"x")
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"v")
# driver.find_element_by_id("su").send_keys(Keys.ENTER)
