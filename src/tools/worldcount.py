#! /usr/bin/python
# coding=UTF-8
# version:python3.x
import os
from src import App


def trunNonalpha(content):
    """剔除全部的非英文字母只保留英文字母的组合"""
    # Nonalpha = "<>()~!@#$%^&*()_+-=;':[]{}?/.,|\"
    alpha = "abcdefjhigklmnopqrstuvwxyz"
    res = ''
    for c in content:
        if c not in alpha:
            c = ' '
        res += c

    return res


def load_dict(file):
    """英文字典/usr/share/dict"""
    englist_dic = []
    with open(file, 'r', encoding='UTF-8') as ff:
        for line in ff.readlines():
            englist_dic.append(line.strip())

    return tuple(englist_dic)


if __name__ == "__main__":
    """由于都是相对较小的文件因此直接进行统计"""

    endict = load_dict(App.resource_file("linux.words"))
    print("englis dic len:", len(endict))
    count_dict = {}
    for dirpath, dirname, filenames in os.walk(u"C:\edocuments"):
        for filepath in filenames:
            f_n = os.path.join(dirpath, filepath)
            print("consume file =>", f_n)
            try:
                f_content = ''
                with open(f_n, 'r', encoding='UTF-8') as ff:
                    for line in ff.readlines():
                        f_content += line

                # 文章字符串前期处理

                f_content = trunNonalpha(f_content.lower())
                strl_ist = f_content.split(" ")

                # 如果字典里有该单词则加1，否则添加入字典
                for ss in strl_ist:
                    # 最长的支持26个字母的单词
                    if 2 < len(ss) <= 26:
                        if ss in count_dict.keys():
                            count_dict[ss] += 1
                        else:
                            count_dict[ss] = 1
            except Exception as e:
                pass

    WEIBOFILE = open("C:/Users/Administrator/Desktop/weibo_daqinghai.txt", "a", encoding='utf_8')
    count_list = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    print(len(count_list))
    for dic in count_list:
        if isinstance(dic, tuple):
            word = dic[0]
            if word in endict:
                ss = word + "," + str(dic[1])
                WEIBOFILE.write(ss + "\n")

    WEIBOFILE.close()
    print(len(count_list))