__author__ = "purelove"
__date__ = "2018/2/25 上午11:41"
import re
from urllib import request
import pymysql
conn = pymysql.connect(host="127.0.0.1", user="root", passwd="purelove", db="home_scrapy", charset="utf8")
cursor = conn.cursor()


#sql ="SELECT * from"
class Spider():
    url = "https://www.panda.tv/cate/lol"
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    title_pattern = '<span class="video-title" title=([\s\S]*?)>'
    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'

    def __fetch_content(self):
        r= request.urlopen(Spider.url)
        htmls =r.read()
        htmls =str(htmls,encoding="utf-8")
        return htmls

    def __analysis(self,htmls):
        root_html = re.findall(Spider.root_pattern,htmls)
        data_list=[]
        for html in root_html:
            name_html = re.findall(Spider.name_pattern,html)
            title_html= re.findall(Spider.title_pattern,html)
            number_html = re.findall(Spider.number_pattern,html)
            data= {'name':name_html,'number':number_html,'title':title_html}
            data_list.append(data)
        return data_list


    def __refine(self,data_list):
        l = lambda data_list:{
            'name':data_list['name'][0].strip(),
            'number':data_list['number'][0],
            'title':data_list['title'][0]
                              }
        #调用lambda表达式
        return map(l,data_list)

    # def __sort(self,data_list):
    #     data_list = sorted(data_list,key=self.__sort_seed)
    #     return data_list
    #
    # def __sort_seed(self,data_list):
    #     r =re.findall('\d*',data_list['number'])
    #     number = float(r[0])
    #     if '万' in data_list['number']:
    #         number = number*10000
    # #     return number
    #
    # def __show(self,data_list):
    #     for data in data_list:
    #         print(data['name']+'~~~~~~~~~~~~~'+data['number']+"~~~~~~~~~~~~"+data['title'])
    def __sql_insert(self,data_list):
        for data in data_list:
            cursor.execute(
                "insert xiongmao_spider(name,number,title) VALUES('{0}', '{1}', {2})".format(data['name'],
                                                                                            data['number'],
                                                                                            data['title']
                                                                                                        )
            )
            conn.commit()

    def go(self):
        htmls = self.__fetch_content()
        data_list = self.__analysis(htmls)
        data_list = list(self.__refine(data_list))
        #data_list = self.__sort(data_list)
        #self.__show(data_list)
        self.__sql_insert(data_list)

xiongmao = Spider()
xiongmao.go()