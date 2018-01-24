#! /usr/bin/python
# coding=UTF-8
# version:python3.x
import os
import hashlib

"""根据文件hash查找指定目录下的重复文件"""
# def get_hash(file_path):
#     f = open(file_path, 'rb')
#     md5_obj = hashlib.md5()
#     while True:
#         d = f.read(1024 * 10)
#         if not d:
#             break
#         md5_obj.update(d)
#     hash_code = md5_obj.hexdigest()
#     f.close()
#     md5 = str(hash_code).lower()
#     return md5


def hash_file(fineName, type="sha256", block_size=64 * 1024):
    """ Support md5(), sha1(), sha224(), sha256(), sha384(), sha512(),
    blake2b(), blake2s(),sha3_224, sha3_256, sha3_384, sha3_512,
    shake_128, and shake_256
    """
    with open(fineName, 'rb') as file:
        hash = hashlib.new(type, b"")
        while True:
            data = file.read(block_size)
            if not data:
                break
            hash.update(data)
        return hash.hexdigest()


if __name__ == '__main__':
    path = "D:/电子书/CODE"
    hash_map = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_name = os.path.join(root, file)
            # file_hash = get_hash(file_name)
            file_hash = hash_file(file_name, "md5")
            info = {'file': file_name, 'hash': file_hash}
            hash_map.append(info)

    result = {}
    for item in hash_map:
        for it in hash_map:
            if it['hash'] == item['hash'] and it['file'] != item['file']:
                result[it['hash']] = "{" + it['file'] + "," + item['file'] + "}"

    for (k, v) in result.items():
        print("hash:", k, "\tfile:", v)
