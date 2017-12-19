
# coding:utf-8

import fileinput
import time

'''测试读取大文件时的各种方法的效率
'''

# 方法1
def method1(file_name):
    count = 0

    with open(file_name) as ff:
        for line in ff:
            count += 1

            #do simething
    return count


#方法2
#处理小文件很方便 大文件就蛋疼了
def method2(file_name):
    count = 0
    for i in fileinput.input(file_name):
        count += 1
    return count


#方法3
def method3(file_name):
    count = 0
    with open(file_name) as ff:
        while 1:
            lines = ff.readlines(1000000)
            if not lines:
                break;
            for line in lines:
                count += 1

    return count


def now():
    ISOTIMEFORMAT = '%Y-%m-%d %X'
    return time.strftime(ISOTIMEFORMAT, time.localtime())


if __name__ == "__main__":
    #hash file size:4G
    big_file = "D:/db/hash/big_pass_2.txt"

    count = 0
    start = now()
    count = method3(big_file)
    end = now()
    print ("method3:" + start + "->" + end + " [result]" + str(count))

    #count =0
    #start = now()
    #count = method2(big_file)
    #end = now()
    #print "method2:"+start+"->"+end+" [result]"+ str(count)

    count = 0
    start = now()
    count = method1(big_file)
    end = now()
    print ("method1:" + start + "->" + end + " [result]" + str(count))