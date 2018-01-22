
# coding:UTF-8

import os


def func_countfileline(filepath):
    """
    统计文件行数
    :param filepath:
    :return:
    """

    num = 0
    thefile = open(filepath, 'rb')
    while True:
        buffer = thefile.read(104857600)
        if not buffer:
            break
        num += buffer.count('\n')
    thefile.close()
    return num + 1


def countfiles(path):
    """
    统计一个目录下的文件数量
    :param path:
    :return:
    """
    file_count = 0
    for root, dirs, files in os.walk(path):
        for f in files:
            f = os.path.join(root, f)
            file_count += 1

    return file_count


def countfilelines(path):
    """
    统计一个目录下的文件的行数
    :param path:
    :return:
    """
    line_count = 0
    for root, dirs, files in os.walk(path):
        for f in files:
            f = os.path.join(root, f)
            line_count += func_countfileline(f)

    return line_count


if __name__ == '__main__':
    print(countfiles("c:/tools/"))
    # print(countfilelines("c:/tools"))
