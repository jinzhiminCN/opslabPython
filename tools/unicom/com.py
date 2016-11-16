import fileinput
# coding:utf-8
"""
  @Summary:用于比较俩个文件
  @ImplementIdea:因为文件中数据不多，所以直接一次性读出到list,然对俩个list做差集
"""
list1 = []
list2 = []

with open("com_1.txt") as f:
    list1 = f.readlines()

#print list1

with open("com_2.txt") as f:
    list2 = f.readlines()
#print list2

ret = set(list1).symmetric_difference(set(list2))

print ret

