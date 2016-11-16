#! /usr/bin/python
# coding:UTF-8

import os, sys, md5, datetime, fileinput, json

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
    # return "{'name':'"+name+"','atime':'"+atime+"','ctime':'"+ctime+"','mtime':'"+mtime+"','md5':'"+filemd5+"'}"
    return "{'name':'" + name + "','ctime':'" + ctime + "','mtime':'" + mtime + "','md5':'" + filemd5 + "'}"


def hashDir(path):
    da = []
    for root, dirs, files in os.walk(path):
        for f in files:
            f = os.path.join(root, f)
            da.append(file_hash(f))
    return da


def hashbakDir(path):
    da = hashDir(path)
    with open('./hash.txt', 'w+') as db:
        for s in da:
            db.write(s + os.linesep)
            print s


def gethash_file(f):
    with open(f) as fs:
        return fs.readlines()


def comHahs(da, db):
    af, afc, afm, bf, bfc, bfm = [], [], [], [], [], []
    for a in da:
        t = eval(a)
        af.append(t['name'])
        afc.append(t['name'] + ":" + t['ctime'])
        afm.append(t['name'] + ":" + t['mtime'])
    for b in db:
        t = eval(b)
        bf.append(t['name'])
        bfc.append(t['name'] + ":" + t['ctime'])
        bfm.append(t['name'] + ":" + t['mtime'])

    print "-----------add file------------"
    for ff in bf:
        if ff not in af:
            print "add > " + ff
    print "----------modify file----------"
    for ff in bfm:
        if ff not in afm:
            print "modify > " + ff


if __name__ == "__main__":

    if len(sys.argv) == 2 and os.path.isdir(sys.argv[1]):
        print "bak -> " + sys.argv[1]
        hashbakDir(sys.argv[1])
    elif len(sys.argv) == 4:
        sys.argv[1] == '-c' and os.path.isdir(sys.argv[2]) and os.path.isfile(sys.argv[3])
        bb = hashDir(sys.argv[2])
        ba = gethash_file(sys.argv[3])
        comHahs(ba, bb)
    else:
        print "Usage:"
        print "\tBak -> hash.py directory"
        print "\tCom -> hash.py -c directory hash.txt"


