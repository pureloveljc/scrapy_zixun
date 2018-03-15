# -*- coding: utf-8 -*-
__time__ = '2018/3/6 0006'
__author__ = 'purelove'

from selenium import webdriver
from scrapy.selector import Selector
import time
browser = webdriver.Chrome(executable_path="E:\pycharmprojects\dangdang\chromedriver.exe")
browser.get('http://e.dangdang.com/pc/reader/index.html?id=1900465429')
time.sleep(5)
browser.find_element_by_css_selector('.reader-wrapper .close').click()
#pic_path = '.\\result\\image\\' + current_time1+'\\' + current_time +'.png'
for i in range(4):
    browser.get_screenshot_as_file('E:\\pycharmprojects\\dangdang\\'+str(i)+'.png')
    browser.find_element_by_id("ddclick-r-trun-right").click()
    time.sleep(3)
#demo_div = browser.find_element_by_css_selector(".text")
#browser.get_screenshot_as_file("E:\pycharmprojects\dangdang\\one.png")
#print (demo_div.get_attribute('value'))

browser.quit()
# for i in range(3):
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
#     time.sleep(3)