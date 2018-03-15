# _*_ encoding:utf-8 _*_
_auther_ = "root"
_date_ = "2017-08-19 下午 5:30"

import requests,os
from bs4 import BeautifulSoup
cur_path = os.getcwd() + '/'

url ="http://www.mzitu.com/page/"
parser = 'html.parser'
header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",'Referer':"http://www.mzitu.com/99566"}
main_page = requests.get(url, headers = header)
print(main_page.text)
preview_page_cnt = 2

for cur_page in range(1, int(preview_page_cnt)+1):
    cur_url = url + str(cur_page)
    cur_page = requests.get(cur_url, headers=header)

    soup = BeautifulSoup(cur_page.text, 'html.parser')
    preview_link_list = soup.find(id='pins').find_all('a', target='_blank')[1::2]
    for link in preview_link_list:
        dir_name = link.get_text().strip().replace('?', '')
        link = link['href']
        soup = BeautifulSoup(requests.get(link).text, parser)

        # 获取图片数量
        pic_cnt = soup.find('div', class_='pagenavi').find_all('a')[4].get_text()
        # 创建目录
        pic_path = cur_path + dir_name
        if os.path.exists(pic_path):
            print('directory exist!')
        else:
            os.mkdir(pic_path)
        os.chdir(pic_path)  # 进入目录，开始下载
        print('download' + dir_name + '...')
        # 遍历获取每页图片的地址
        for pic_index in range(1, int(pic_cnt) + 1):
            pic_link = link + '/' + str(pic_index)
            cur_page = requests.get(pic_link, headers=header)
            soup = BeautifulSoup(cur_page.text, parser)
            pic_src = soup.find('div', 'main-image').find('img')['src']
            pic_name = pic_src.split('/')[-1]
            f = open(pic_name, 'wb')
            f.write(requests.get(pic_src, headers=header).content)
            f.close()
        os.chdir(cur_path)  # 完成下载，退出目录
    print('下载完成')
