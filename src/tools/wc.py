# coding:UTF-8

import os


def func_countfileline(filepath):
    num_col = 0
    try:
        for index, line in enumerate(open(filepath, 'r', encoding='UTF-8')):
            num_col += 1
    except Exception as e:
        print("error count :" + filepath)
    return num_col


def file_extension(file):
    return os.path.splitext(file)[1]


if __name__ == '__main__':
    path = 'C:/xwtech/ydb/qhmccClientZb/'
    # exten_list = ['.java', '.xml', '.properties','.html','.js','.css']
    exten_list = ['.java']
    line_count = 0
    file_count = 0
    for root, dirs, files in os.walk(path):
        for f in files:
            f = os.path.join(root, f)

            if os.path.splitext(f)[1].lower() in exten_list:
                # print(f + "==>" + os.path.splitext(f)[1].lower())
                file_count += 1
                line_count += func_countfileline(f)

    print('文件数：' + str(file_count) + '\n总行数:' + str(line_count))

