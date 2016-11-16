import fileinput

for line in fileinput.input("1.txt"):
    lists = line.split(':')

    print lists[0].strip() + ",--" + lists[1].strip();