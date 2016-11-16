#!/usr/bin/python
# coding:utf-8

import generateUUID

'''
    生成一组UUID
'''
if __name__ == '__main__':
    for x in xrange(50):
        print str(generateUUID.uuid1()).replace('-', '').upper()

