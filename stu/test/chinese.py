import re

pchinese = re.compile('([\u4e00-\u9fa5]+)+?')

m = pchinese.findall(unicode("Sん夜色♂DEVIL".encode("latin1"), "utf-8", 'ignore'))
print m