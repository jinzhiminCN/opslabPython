#!/usr/bin/python
# coding:utf-8

import requests
import Menu

from conf import constant


_cookie = []


def login():
    sessionid = requests.get(constant.host, constant.headers).cookies['JSESSIONID']

    url = constant.host + "login.do"
    data = {
        'userCode': '4004',
        'password': '1',
        'JSESSIONID': sessionid
    }
    r = requests.post(url, data, constant.headers)

    print "login in successful..."
    return r.cookies


if __name__ == "__main__":
    cookies = login()
    menu = Menu.Menu(cookies)
    menu.cmdloop()
