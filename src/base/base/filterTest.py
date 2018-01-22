
# coding:UTF-8

"""
    @author: neptune
    @time: 2014-02-20
    @descript: 主要演示filter函数的使用方法
"""


def filter_key(keys):
    list_key = ['hjt', 'xjp', 'mzd', 'wjb', 'lq']
    if keys in list_key:
        return False
    else:
        return True


if __name__ == "__main__":
    strs = "china's load is xjp"
    print(type(filter(filter_key, strs)))
    print(filter(filter_key, strs))
    list_str = strs.split(" ")
    print(" ".join(filter(filter_key, list_str)))
