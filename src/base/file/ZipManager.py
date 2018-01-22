
# encoding:utf-8

import os, zipfile, shutil


def zip_dir(dirname, zipfilename):
    """
    @函数目的: 压缩指定目录为zip文件
    @参数说明：dirname为指定的目录，zipfilename为压缩后的zip文件路径
    """
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else:
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))

    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)

    for tar in filelist:
        arcname = tar[len(dirname):]
        # print arcname
        zf.write(tar, arcname)

    zf.close()


def unzip_file(zipfilename, unziptodir):
    """
    | ##@函数目的: 解压zip文件到指定目录
    | ##@参数说明：zipfilename为zip文件路径，unziptodir为解压文件后的文件目录
    | ##@返回值：无
    | ##@函数逻辑：
    """
    if not os.path.exists(unziptodir):
        os.mkdir(unziptodir)
    zfobj = zipfile.ZipFile(zipfilename)
    for name in zfobj.namelist():
        name = name.replace('\\', '/')

        if name.endswith('/'):
            p = os.path.join(unziptodir, name[:-1])
            if os.path.exists(p):
                # 如果文件夹存在，就删除之：避免有新更新无法复制
                shutil.rmtree(p)
            os.mkdir(p)
        else:
            ext_filename = os.path.join(unziptodir, name)
            ext_dir = os.path.dirname(ext_filename)
            if not os.path.exists(ext_dir):
                os.mkdir(ext_dir)
            outfile = open(ext_filename, 'wb')
            outfile.write(zfobj.read(name))
            outfile.close()