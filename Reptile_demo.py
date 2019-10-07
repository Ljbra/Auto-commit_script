# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 21:12:51 2019

@author: 焦少
"""

#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
import time
import os
# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs


scores_data = []
path = "C:/Users/Libra/Desktop/test" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
s = []
for file in files: #遍历文件夹
     if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
          file_str = path+"/"+file
          s.append(file_str) #每个文件的文本存到list中


#创建浏览器对象
driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')

driver.get("http://www.pigai.org/?c=v2&a=write&rid=10")

time.sleep(4)
driver.find_element_by_name("username").send_keys("17860612167")
driver.find_element_by_name("password").send_keys("jxytjiaowb")


# 模拟点击登录
driver.find_element_by_xpath("//button[@class='loginBtn']").click()


for i in range(2):
    with open(s[i], 'r') as f:
        data = f.read()
    driver.find_element_by_xpath("//ul[@id='header_navi']/li[2]/a").click()
    driver.find_element_by_id("contents").send_keys(data)
    driver.find_element_by_id("dafen").click()
    
    time.sleep(3)
    soup = bs(driver.page_source, "lxml")
    soup.find()
    element = soup.find_all("span", {"class" : "circles-integer"},limit=1)
    element1 = soup.find_all("span", {"class" : "circles-decimals"},limit=1)
    for name, number in zip(element1, element):
        scores = number.get_text().strip() + u"." + name.get_text().strip()
    file_name = str(i+1) +":   " +scores+"\n"
    scores_data.append(file_name)
f = open("C:/Users/Libra/Desktop/test/record.txt",'a')
f.writelines(scores_data)
f.close()

#
## 获取当前url
#print driver.current_url

# 关闭当前页面，如果只有一个页面，会关闭浏览器
# driver.close()

# 关闭浏览器
#driver.quit()