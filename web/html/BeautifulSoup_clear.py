#! /usr/bin/python
# encoding=UTF-8

from bs4 import BeautifulSoup
import os


file_object = open('E:/workspace/python/web/pythonModuleDemo/download/arrow/Arrow.html')
try:
    all_the_text = file_object.read()

    soup = BeautifulSoup(all_the_text, "html.parser")
    disqus_thread = soup.find('div', id='disqus_thread')
    if disqus_thread:
        disqus_thread.extract()

    div = soup.find('div', style=re.compile(r'width:300px*')
    if div:
        print div.extract()
    print soup.prettify()
    finally:
    file_object.close()




