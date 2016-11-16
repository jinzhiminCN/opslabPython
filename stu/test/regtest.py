#! /usr/bin/python
# coding:utf-8

import re

reg = re.compile(u"[~!@#$%^&*()_+<>?:,./;'，。、‘：“《》？~！@#￥%……（）]")
str = re.sub(reg, '', u"123~!@#$%^&*()_+<>?:,./;'，。、‘：“《》？~！@#￥%……（）")
print str