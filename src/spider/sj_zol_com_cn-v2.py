#! /usr/bin/python
# coding=UTF-8
# version:python3.x
import os
import requests
from lxml import etree

cur_path = os.path.dirname(__file__)
file_path = os.path.join(cur_path,"image")
if not os.path.exists(file_path):os.mkdir(file_path)

class LoadImage():

    def __init__(self,page_num=1,base_url="http://sj.zol.com.cn/bizhi/new_%d.html"):
        """
        :param base_url: 爬取网页的url
        :param page_num: 爬取第几页数
        """
        # 这个网站貌似没有做什么限制，不加headers也是可以的，可以直接请求，以免爬取数据有限制，这里我加上了
        self.s = requests.session()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            "Upgrade-Insecure-Requests":"1"
        }

        self.base_url = base_url
        self.page_num = page_num

    def load_page(self):
        url = (self.base_url)%self.page_num  # 我们的请求地址进行拼接
        res = self.s.get(url,headers=self.headers).text  # 获取网页
        html = etree.HTML(res)  # 使用lxml转换为html格式的数据
        index_links = html.xpath("//div/ul[1]/li/a[@class='pic']/@href")  # 获取页面url
        file_titles = html.xpath("//li[@class='photo-list-padding']/a[@class='pic']/@title")  # 获取页面图片库名称
        return index_links,file_titles

    def load_image(self):
        index_link,file_titles = self.load_page()
        url_and_title = zip(index_link,file_titles)  # 将返回的数据一一对应，下标0为图片库url，1为标题
        for u_t in url_and_title:
            save_path = os.path.join(file_path,u_t[1])  # 将标题与image拼接，后期爬取的图片会存放在标题对应的目录下
            if not os.path.exists(save_path):os.mkdir(save_path)  # 判断路径是否存在，不存在就创建目录

            res_url = "http://sj.zol.com.cn%s"%u_t[0]  # 页面上获取的图片链接仅为路径，这里需要url拼接
            res = self.s.get(res_url,headers=self.headers).text
            html = etree.HTML(res)
            img_url_list = html.xpath("//ul[@id='showImg']/li/a/@href")

            for img_url in img_url_list: # 循环图片链接列表，依次写入文件中去
                print(img_url)
                self.load_gqimage('http://sj.zol.com.cn'+img_url,save_path)

                # with open("%s/%s"%(save_path,img_name),"wb") as f:
                #     f.write(img_res.content)
                #     print("%s正在下载"%img_name)


    def load_gqimage(self,detail_url,save_path):
        res = self.s.get(detail_url,headers=self.headers).text  # 获取网页
        html = etree.HTML(res)  # 使用lxml转换为html格式的数据
        index_links = html.xpath("//dl/dd/a[1]/@href")  # 获取页面url
        res = self.s.get('http://sj.zol.com.cn'+index_links[0],headers=self.headers).text  # 获取网页
        html = etree.HTML(res)
        image_url = html.xpath("//img/@src")[0]
        img_res = self.s.get(image_url,headers=self.headers)
        img_name = image_url.split("/")[-1]  # 图片名称
        with open("%s/%s"%(save_path,img_name),"wb") as f:
                    f.write(img_res.content)
                    print("%s正在下载"%img_name)
if __name__ == '__main__':

    for i in range(1,5): # 直接下载第1页到第4页的图片
        lo_img = LoadImage(page_num=i)
        lo_img.load_image()
