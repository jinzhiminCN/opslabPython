
# encoding=UTF-8

# @descript:check url exists?
# for python2.x
# python2.x和python3.x的区别还是蛮大的，逾期折腾这些不如直接用requests

# import html.parser as h
# import urllib
# import urllib.request
#
# class CheckURL(h.HTMLParser):
#     available = True
#
#     def handle_data(self, data):
#         if "404 Not Found" in data or "Error 404" in data:
#             self.available = False
#
#
# for url in ['admin', 'test', 'phpinfo.php', 'sys']:
#     new_url = urllib.parse.urljoin("http://www.python.org", url)
#     fp = urllib.request.urlopen(new_url)
#     data = fp.read()
#     fp.close()
#
#     p = CheckURL()
#     p.feed(data)
#     p.close()
#
#     if p.available:
#         print(new_url.ljust(40), '====>OK')
#     else:
#         print(new_url.ljust(40), '====>404')
