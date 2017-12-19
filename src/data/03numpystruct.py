
# coding:UTF-8

"""在C语言中我们可以通过struct关键字定义结构类型，
结构中的字段占据连续的内存空间，每个结构体占用的内存大小都相同，
因此可以很容易地定义结构数组。和C语言一样，
在NumPy中也很容易对这种结构数组进行操作。
只要NumPy中的结构定义和C语言中的定义相同，
NumPy就可以很方便地读取C语言的结构数组的二进制数据，
转换为NumPy的结构数组。"""

import numpy as np

# 定义一个结构体 names字段结构体的类型，float定义类型,还有其他的方式定义结构体，但是没有这种方式简洁
# S32 : 32个字节的字符串类型，由于结构中的每个元素的大小必须固定，因此需要指定字符串的长度
# i : 32bit的整数类型，相当于np.int32
# f : 32bit的单精度浮点数类型，相当于np.float32
struct_person = np.dtype({
    'names': ['name', 'age', 'weigth'],
    'formats': ['S32', 'i', 'f']
})

a = np.array([("Zhang", 32, 75.5), ("Wang", 24, 65.2)], dtype=struct_person)
print(a)
print(a[0]['name'])
print(a[0]['age'])
# 获取所有的名字
print(a[:]['name'])
# 输出二进制形式
print(a.tostring)
