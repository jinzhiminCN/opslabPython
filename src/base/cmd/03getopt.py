
# coding=UTF-8
# version=3.x

import sys, getopt

"""get param-list from command-line"""


def usage():
    print("""
        -h(--help)              显示帮助文档
        -s(--save) save_file    结果保持的指定的文件
    """)


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hs:", ["help", "save="])
        if not opts:
            usage()
            exit()

        for opt, value in opts:
            if opt in ('-h', '--help'):
                usage()
                exit()
            if opt in ('-s', '--save'):
                print("result save to %s" % value)
    except getopt.GetoptError:
        usage()
        exit()
