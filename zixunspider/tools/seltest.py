# -*- coding: utf-8 -*-
__time__ = '2018/3/6 0006'
__author__ = 'purelove'
# from selenium import webdriver
# browser = webdriver.Chrome(executable_path="E:\pycharmprojects\zixunspider\chromedriver.exe")
# browser.get("http://news.zhulong.com/")
# import time
# time.sleep(5)
# for i in range(100):
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
#     browser.find_element_by_css_selector('.section-more #pull-more').click()
#     time.sleep(3)
# browser.quit()


import re
import datetime
create = ['时间：2018年02月05日 \xa0 \xa0\xa0\xa0\xa0\xa0  来源：', '  \xa0\xa0 \xa0\xa0\xa0\xa0 作者：邓媛雯']
l ="".join(create)
create_date = re.findall('.*?(\d{4}[-年]\d{1,2}[-月]\d{1,2}[-日])', l)

create_date = create_date[0].replace('年','-')
create_date = create_date.replace('月','-')
create_date = create_date.replace('日','')
print(create_date)

create_date = datetime.datetime.strptime(create_date, "%Y-%m-%d").date()
print(type(create_date))

all_urls =[]
for x in range(1, 280):  # [1~279]
    url = 'http://www.archcollege.com/cat/news?t=a&cname=news&orderby=&page={0}'.format(x)
    all_urls.append(url)
print(all_urls)