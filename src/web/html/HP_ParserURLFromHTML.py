
# coding:UTF-8

# for python2.x
# python2.x和python3.x的区别还是蛮大的，逾期折腾这些不如直接用requests

#Parser HTML and get all url
# import HTMLParser
# import urllib
#
#
# class parserLinks(HTMLParser.HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         if tag == 'a':
#             for name, value in attrs:
#                 if name == 'href':
#                     print self.get_starttag_text(), value
#
#
# if __name__ == '__main__':
#     urlparser = parserLinks()
#     urlparser.feed(urllib.urlopen("http://www.linuxidc.com/topicnews.aspx?tid=14").read())