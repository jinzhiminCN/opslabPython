#!/usr/bin/env python
# coding=utf-8

#
# 了解编码的最好的方式就是采用不同的编码编码统一段字符串，并查看字节序列的区别
#
import binascii


def to_hex(t, nbytes):
    chars_per_item = nbytes * 2
    hex_version = binascii.hexlify(t)
    return ' '.join(
        hex_version[start:start + chars_per_item]
        for start in range(0, len(hex_version), chars_per_item)
    )


text = u'青海'

print 'Raw      :', repr(text)
print 'UTF-8    :', to_hex(text.encode('utf-8'), 1)
print 'UTF-16   :', to_hex(text.encode('utf-16'), 2)
print 'GBK      :', to_hex(text.encode('gbk'), 2)

