#! /usr/bin/python
# coding:UTF-8

#演示通过HTMLParser解析并处理特定的HTML标签
from HTMLParser import HTMLParser


class ParserForm(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if (tag == "form"):
            print "标签命:", tag
            print "属性=》attr‘s type：", type(attrs), attrs


if __name__ == '__main__':
    print "演示通过HTMLParser解析特定的HTML标签"
    ph_parser = ParserForm()
    ph_parser.feed("""
        <html>
    <head>
        <title>this is tile</title>
    </head>
    <body>
        <form action="help.php" method="post">
            username:<input type="text" id="name"></input>
        </form>
    </body>
    </html>
    """)