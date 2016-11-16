#! /usr/bin/python
# coding:UTF-8

"""
    每个class文件必须以同样的字节开始，一般被称为魔数:0xCAFEBABE
"""
if __name__ == 'main':
    with open("1.class", "rb") as f:
        str = f.read(4)
        print [hex(ord(x)) for x in str]

    with open("2.class", "rb") as f:
        str = f.read(4)
        print [hex(ord(x)) for x in str]
