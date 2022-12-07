import sys

def main():
    get_priorities()

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

main()