import sys
# import queue

def main():
    simulation()

def simulation():
    filename = sys.argv[1]
    f = open(filename, 'r')

    stacks = {}
    line = f.readline()
    while line != '\n':
        for i in range(0, len(line), 4):
            if line[i:i+3] != '   ':
                val = (i//4) + 1
                if val in stacks:
                    stacks[val].append(line[i+1])
                else:
                    stacks[val] = [line[i+1]]        
        line = f.readline()

    instructions = f.readlines()

    for line in instructions:
        line = line.split()
        for i in range(int(line[1])):
            stacks[int(line[5])].insert(0,stacks[int(line[3])].pop(0))

    top_blocks = ''
    for i in range(1,len(stacks)+1):
        top_blocks += stacks[i][0]
    print(f'The top layer of blocks is {top_blocks}')

main()