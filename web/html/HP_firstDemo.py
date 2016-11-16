#! /usr/bin/python
# coding:UTF-8
#演示通过HTMLParser解析HTML文件
from HTMLParser import HTMLParser

#从HTMLParser类集成一些有用的方法
class FirstHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "a start tag:", tag

    def handle_endtag(self, tag):
        print "a end tag:", tag

    def handle_data(self, data):
        print "some data:", data


if __name__ == '__main__':
    html_parser = FirstHTMLParser()
    html_parser.feed("""
        <html>
        <head>
            <title>this is tile</title>
        </head>
        <body>
            <h1>this is some data</h1>
        </body>
        </html>
    """)