#! /usr/bin/python
# coding=UTF-8
# version:python3.x
# author: monsoon

import json
import os
import traceback
from googletrans import Translator

translator = Translator(service_urls=[
    'translate.google.cn'
])

for dirpath, dirname, filenames in os.walk(u"C:\workspace\mancmdline\linux-commands"):
    for filepath in filenames:
        f_n = os.path.join(dirpath, filepath)
        print("consume file =>", f_n)

        try:
            f_content = ''
            with open(f_n, 'r+', encoding='UTF-8') as ff:
                for line in ff.readlines():
                    if line.startswith('#'):
                        trans_content = line.replace("# ", "").strip()
                        print(trans_content)
                        trans_line = translator.translate(trans_content, dest='zh-CN').text
                        line += '#' + trans_line + '\n'

                    f_content += line

                ff.seek(0)
                ff.truncate()
                ff.write(f_content)

            print(f_content)
        except Exception as e:
            traceback.print_exc()

