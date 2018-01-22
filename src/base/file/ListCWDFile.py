
# coding:UTF-8
def recursion_listFile(pwd):
    if os.path.isfile(pwd):
        print (pwd.ljust(20), os.stat(pwd))
    else:
        recursion_listFile(pwd)


import os

if __name__ == '__main__':
    """列出当前目录及当前目录下的文件"""
    #获取当前目录的路径
    cwd = os.getcwd()
    print ("cwd's type=>", type(cwd), cwd)
    listdir = os.listdir(cwd)
    print ("listdir's type=>", type(listdir), listdir)

    #iterator
    for tmp_file in listdir: recursion_listFile(tmp_file)
