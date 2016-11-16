#! /usr/bin/python
# coding=UTF-8

import sys


def info(datatype, spacing=15, collapse=1):
    """Print methods and doc-strings wtih object"""

    method_list = [method for method in dir(datatype) if callable(getattr(datatype, method))]
    process_func = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)

    print "\n".join(["%s %s" %
                     (method.ljust(spacing), process_func(str(getattr(datatype, method).__doc__)))
                     for method in method_list])


def help_me():
    print "*.py datatype"
    print "as *.py list"


if __name__ == "__main__":
    if len(sys.argv) == 2:
        info(sys.argv[1])
    else:
        help_me()
