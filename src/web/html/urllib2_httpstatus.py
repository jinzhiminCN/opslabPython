
# encoding=UTF-8

# for python2.x
# python2.x和python3.x的区别还是蛮大的，逾期折腾这些不如直接用requests

# import urllib2
#
#
# print "对于请求的请求可以通过response.getcode()就能获得"
# print "对于错误的请求，urllib2会抛出异常，这时可以检测异常对象的code属性"
#
# response = urllib2.urlopen('http://www.baidu.com')
# print response.getcode()
#
# try:
#     response = urllib2.urlopen('http://127.0.0.1/admin.php')
# except urllib2.HTTPError, e:
#     print e.code
