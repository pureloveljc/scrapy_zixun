# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = '2018/4/10 14:10'
from selenium import webdriver
from pyquery import PyQuery as pq
import time
SERVICE_ARGS = ['--load-images=false', '--disk-cache-path=true']
#driver = webdriver.PhantomJS(service_args=SERVICE_ARGS, executable_path='E:\ljcprojects\other_spider\phantomjs.exe')
driver = webdriver.Chrome(executable_path="E:\ljcprojects\googleSpider\chromedriver.exe")  #用chorm浏览器

driver.get("https://trends.google.com/trends/home/all/PH")
time.sleep(5)
#driver.set_window_size(1400, 900)

for i in range(8):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
    time.sleep(3)

html = driver.page_source
doc = pq(html.encode('utf-8'))
items = doc('#trending-stories-container .md-list-block .md-list-item-block').items()
count = 0
output_file =open("E:/"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+".txt","w",encoding='utf8')
for item in items:
    value =item.find('.title').text().strip()
    count+=1

    # data = {
    #     'title': value,
    #     'count': count
    # }
    output_file.write("count:"+str(count)+"~~~~~"+"title:"+value +"\n")
    print(value+"写入成功")
    time.sleep(5)

output_file.close()