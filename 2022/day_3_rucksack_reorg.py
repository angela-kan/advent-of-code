import sys

def main():
    get_badges()

def get_priorities():
    filename = sys.argv[1]
    f = open(filename, "r")
    total = 0
    for line in f.readlines():
        d = {}
        for i in range(int(len(line)/2)):
            d[line[i]] = i
        i+=1
        while i<len(line):
            if line[i] in d:
                if ord(line[i]) > 90:
                    total += ord(line[i])-96
                else:
                    total += ord(line[i])-64+26
                break
            i+=1
    print(f'The total sum of priorities is {total}')

def get_badges():
    filename = sys.argv[1]
    f = open(filename, "r")
    total = 0

    lines = f.readlines()
    for i in range(0,len(lines), 3):
        elf1 = set(lines[i].strip())
        elf2 = set(lines[i+1].strip())
        elf3 = set(lines[i+2].strip())

        badge = elf1.intersection(elf2).intersection(elf3).pop()
        total += get_priority(badge)

    print(f'The total priorities of the badges is {total}')

def get_priority(item):
    if ord(item) > 90:
        return ord(item)-96
    else:
        return ord(item)-64+26
        

main()