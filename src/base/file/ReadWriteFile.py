
# coding:UTF-8
import sys


def operation_file(file_name):
    try:
        h_file = open(file_name, 'r', 1)
        try:
            readlines = h_file.readlines();
            print (readlines)
        finally:
            h_file.close()
    except IOError:
        print ("IOError")


def operation_wrtiefile(file_name, strs):
    try:
        h_file = open(file_name, 'w', 1)
        try:
            h_file.write(strs)
        finally:
            h_file.close()
    except IOError:
        print ("IOError")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("usage:*.py path/file_name")
    else:
        operation_file(sys.argv[1])
    print ("write file:")
    strs = """
        All that city!you just couldn't see an end to it.
        The end? please? can you please just show me where is ends?
        ...
        One woman,onw house,one piece of land to call your own
        One landscape to look at,on way to die!
        All that world just weighing down on you.
        You don't even know where it comes to and end.
        ...!
    """
    print (strs)
    operation_wrtiefile("aplanforme.txt", strs)
    
    