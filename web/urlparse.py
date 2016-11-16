#! /usr/bin/python
# coding:UTF-8

import sys, getopt, urlparse


if __name__ == '__main__':
    site = "http://www.baidu.com/index.php"
    params = ""
    opts, agrs = getopt.getopt(sys.argv[1:], "i", ["input"])
    for opt, value in opts:
        if opt in ('i', 'input'):
            params = value

    #print params
    url = urlparse.urlparse(site + "?" + params)
    print url.query
