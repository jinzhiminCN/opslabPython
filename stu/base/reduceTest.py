#! /usr/bin/python
# coding:UTF-8
'''
    @author: neptune
    @time: 2014-02-20
    @descript: 主要演示filter函数的使用方法
'''


def reduce_function(x, y):
    return x * 10 + y


if __name__ == "__main__":
    li = range(10)
    value = reduce(reduce_function, li, 1)
    print value
    value = reduce(lambda x, y: x * 10 + y, li, 1)
    print value
