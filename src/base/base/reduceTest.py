
# coding:UTF-8

"""
    @time: 2014-02-20
    @descript: 主要演示filter、man、reduce函数的使用方法
"""


def list_filter(x):
    if x % 2 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    # filter()为已知的序列的每个元素调用给定的布尔函数，调用中，返回值为非零的元素将被添加至一个列表中
    # python 2.xfilter函数会直接输出结果。但在python3中做了些修改，输出前需要使用list()进行显示转换
    ls = list(filter(list_filter, [1, 2, 3, 42, 67, 16]))
    print(ls)
