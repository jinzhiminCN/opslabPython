#! /usr/bin/python
# coding:UTF-8
'''
    @author: neptune
    @time: 2014-02-20
    @descript: 主要演示函数的定义，以及一些常用的操作和技巧
'''
import sys


def main(func_name="help"):
    slefMod = __import__(__name__)
    fun = getattr(slefMod, "func_%s" % func_name)
    fun()


#=======================================================================================
#函数定义的语法:
#def function_name(param_list):
#    pass  函数体，注意缩进
#=======================================================================================
def func_first(arg1):
    print arg1;


if __name__ == '__main__':
    for arg in sys.argv: print arg