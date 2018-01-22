
# coding:UTF-8

import os, sys


def removeBom(file):
    with open(file, "rb") as f:
        str = f.read(3)
        if "0xef0xbb0xbf" == "".join(list([hex(ord(x)) for x in str])):
            print (file + "-UTF8-BOM File")
            buffer = f.read(999999999)
            print ([hex(ord(x)) for x in buffer])


def IteatorDir(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            f = os.path.join(root, f)
            removeBom(f)


if __name__ == '__main__':
    if len(sys.argv) >= 3 and (sys.argv[1] == '-f' or sys.argv[1] == '-d'):
        if sys.argv[1] == '-f' and os.path.isfile(sys.argv[2]):
            print (sys.argv[2],)
            removeBom(sys.argv[2])
        elif sys.argv[1] == '-d' and os.path.exists(sys.argv[2]):
            IteatorDir(sys.argv[2])
        else:
            print ('-- 文件(夹)' + sys.argv[2] + '不存在')
    elif len(sys.argv) == 1:
        print (IteatorDir(os.getcwd()))
    else:
        print ('-- 参数说明 ：')
        print ('    1. ' + sys.argv[0] + ' -f' + ' filename')
        print ('    2. ' + sys.argv[0] + ' -d' + ' directory')
        print ('    3. ' + sys.argv[0] + ' ')
