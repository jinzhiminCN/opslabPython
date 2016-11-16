#!/usr/bin/python
# coding:utf-8

import re

regex_email = re.compile(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b", re.IGNORECASE)


def isMail(email):
    if regex_email.search(email):
        return email
    return '-'


if __name__ == "__main__":
    print isMail("wwww")
    print isMail("")
    print isMail('y')
    print isMail("1@1.com")
    print isMail("cy_qing@163.com")