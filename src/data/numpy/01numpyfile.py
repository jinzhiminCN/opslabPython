# coding:UTF-8

"""文件名和文件对象"""
import numpy as np
from conf import App

file_name = App.BASE_TEMP + "numpy_result.npy"
print(file_name)
a = np.arange(8)
b = np.add.accumulate(a)
c = a + b
print(a)
print(b)
print(c)
f = open(file_name, "wb")
# 顺序将a,b,c保存进文件对象f
np.save(f, a)
np.save(f, b)
np.save(f, c)
f.close()

ff = open(file_name, "rb")
# 顺序从文件对象f中读取内容
print(np.load(ff))
print(np.load(ff))
print(np.load(ff))


