
# coding=UTF-8
# version:python3.x

"""从文件中导入数据"""
import numpy as np
from src import App

file_name = App.BASE_TEMP + "numpy_arrry1.txt"

with open(file_name,'a') as ff:
    array = np.random.rand(10,2)
    for i in range(10):
        ff.write("%f %f\n"%(array[i,0],array[i,1]))

# 将数据读取出来，存为numpy数组
a = np.loadtxt(file_name)
print(a)

# 将数据存储文件并读入，指定分隔符
file_name = App.BASE_TEMP + "numpy_arrry2.txt"
with open(file_name,'a') as ff:
    array = np.random.rand(10,2)
    for i in range(10):
        ff.write("%f,%f\n"%(array[i,0],array[i,1]))

b = np.loadtxt(file_name,delimiter=",")
print(b)