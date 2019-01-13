#! /usr/bin/python
# coding=UTF-8
# version:python3.x
# author: monsoon

from googletrans import Translator

translator = Translator(service_urls=[
    'translate.google.cn'
])

trans_line = translator.translate("hello world", dest='zh-CN').text
print(trans_line)