# coding=UTF-8

import getopt
import sys

"""get param-list from command-line"""


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hg:d")
        print("opt's type=>", type(opts), opts)
        print("args's type=>", type(args), args)

        for opt, arg in opts:
            print(opt, arg)

    except getopt.GetoptError:
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])
