# coding:UTF-8
# version 3.4

import re

# 对于大文件而言直接open,read更为快些
# for line in fileinput.input(u"catalina.2017-04-03.txt",
#                             openhook = fileinput.hook_encoded("UTF-8")):
#         #print(line,end="")
#         line.split("\s")
pattern = re.compile(r"^[a-zA-Z].*Exception")

at_error = {}
with open('catalina.out', 'rt', encoding='utf-8', buffering=1024) as f:
    for line in f:
        if pattern.match(line):
            print(line, end="")

        if line.startswith("	at"):
            package = line.replace("	at", "").strip()
            if package in at_error:
                count = at_error.get(package) + 1
                at_error[package] = count
            else:
                at_error[package] = 1


                # if "Exception" in line :
                #     if re.match('Exception',line):
                #         print(line)

                ## 统计异常信息
                # if "Exception in " in line:
                #     print(line)

                #     error_Info = line
                #     isException = True
                #
                # if isException:
                #     error_Info += line
                #     if re.match(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",line):
                #         isException = False
                # print(error_Info,end="")


# for key in at_error:
#     print(key+" =>" + str(at_error.get(key)))
