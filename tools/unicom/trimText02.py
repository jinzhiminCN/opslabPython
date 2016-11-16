import fileinput


for line in fileinput.input("2.txt"):
    line = "'" + line.replace('\n', '') + "',"
    print line