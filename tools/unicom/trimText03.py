import fileinput

for line in fileinput.input("3.txt"):
    line = line.split(" ")
    print line


