#! /usr/bin/python
# coding=UTF-8
# version:python3.x
# author: monsoon

import os
import traceback
import re

translate_line_partter = "^[a-zA-Z>\-]{1,}$"

for dirpath, dirname, filenames in os.walk(u"C:\workspace\mancmdline\windows-commands"):
    for filepath in filenames:
        f_n = os.path.join(dirpath, filepath)
        print("consume file =>", f_n)

        try:
            f_content = ''
            with open(f_n, 'r+', encoding='UTF-8') as ff:
                for line in ff.readlines():
                    if re.match(translate_line_partter,line):
                        print(line)

                # ff.seek(0)
                # ff.truncate()
                # ff.write(f_content)

            print(f_content)
        except Exception as e:
            traceback.print_exc()

        break