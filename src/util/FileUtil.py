import os
import zipfile
import hashlib
import shutil

"""文件相关的一些方法
"""

def hash_file(fine_name, type="sha256", block_size=64 * 1024):
    """ Support md5(), sha1(), sha224(), sha256(), sha384(), sha512(),
    blake2b(), blake2s(),sha3_224, sha3_256, sha3_384, sha3_512,
    shake_128, and shake_256
    """
    with open(fine_name, 'rb') as file:
        hash = hashlib.new(type, b"")
        while True:
            data = file.read(block_size)
            if not data:
                break
            hash.update(data)
        return hash.hexdigest()


def dir_size(dir_path):
    """获取目录的大小"""
    size = 0
    for root, dirs, files in os.walk(dir_path):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])

    return str(round(size / 1024 / 1024, 2)) + "M"


def trim_path(file_name):
    """返回标准的路径"""
    return os.path.normpath(file_name).replace("\\", "/")


def dir_info(dir_path, path_level):
    """返回指定路面下的path_level内的文件和文件夹"""
    re_list = []
    if path_level == 0:
        return re_list
    for file_name in os.listdir(dir_path):
        path_name = os.path.join(dir_path, file_name)
        if os.path.isfile(path_name):
            re_list.append(trim_path(path_name))
        if os.path.isdir(path_name):
            re_list.append(trim_path(path_name))
            re_list += dir_info(path_name, path_level - 1)
    return re_list


def del_path(path):
    """删除指定的目录，支持多级目录"""
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_path(c_path)
        else:
            os.remove(c_path)
    os.rmdir(path)



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