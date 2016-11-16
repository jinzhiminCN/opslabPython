#! /usr/bin/python
# coding:UTF-8

import os, sys, md5, datetime, fileinput

reload(sys)
sys.setdefaultencoding("UTF-8")

encoding = sys.getfilesystemencoding()


def FileMd5(f):
    m = md5.new()
    o_f = open(f)
    while True:
        d = o_f.read(8096)
        if not d:
            break
        m.update(d)
    return m.hexdigest()


def time(t):
    tt = datetime.datetime.fromtimestamp(t)
    return tt.strftime('%Y-%m-%d %H:%M:%S')


def file_hash(f):
    name = str(f).decode(encoding).replace("\\", "/")
    ctime = time(os.path.getctime(f))
    mtime = time(os.path.getmtime(f))
    atime = time(os.path.getatime(f))
    filemd5 = FileMd5(f)
    #return "{'name':'"+name+"','atime':'"+atime+"','ctime':'"+ctime+"','mtime':'"+mtime+"','md5':'"+filemd5+"'}"
    return "{'name':'" + name + "','ctime':'" + ctime + "','mtime':'" + mtime + "','md5':'" + filemd5 + "'}"


def hashDir(path):
    da = []
    for root, dirs, files in os.walk(path):
        for f in files:
            f = os.path.join(root, f)
            da.append(file_hash(f))
    return da


def hashbakDir(path):
    try:
        h_file = open("./hash.txt", 'w', 1)
        try:
            for s in hashDir(path):
                h_file.write(s + os.linesep)
        finally:
            h_file.close()
    except IOError:
        print "IOError"


if __name__ == "__main__":

    if len(sys.argv) == 2 and os.path.isdir(sys.argv[1]):
        print "bak -> " + sys.argv[1]
        hashbakDir(sys.argv[1])

    else:
        print "Usage:"
        print "\tBak -> hash.py directory"
