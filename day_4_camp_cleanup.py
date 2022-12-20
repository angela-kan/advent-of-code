import sys

def main():
    get_contained_pairs()
    get_overlaps()

def get_contained_pairs():
    filename = sys.argv[1]
    f = open(filename, 'r')
    overlaps = 0
    for line in f.readlines():
        pair = [slot.split('-') for slot in line.strip().split(',')]
        pair = [[int(x) for x in i] for i in pair]
        pair.sort()
        
        if pair[0][0] < pair[1][0] and pair[0][1] < pair[1][1]:
            continue
        else:
            overlaps += 1
    print(f'The number of contained pairs is {overlaps}.')

def get_overlaps():
    filename = sys.argv[1]
    f = open(filename, 'r')
    overlaps = 0
    for line in f.readlines():
        pair = [slot.split('-') for slot in line.strip().split(',')]
        pair = [[int(x) for x in i] for i in pair]
        pair.sort()
    
        if pair[1][0] > pair[0][1]:
            continue
        else:
            overlaps += 1

    print(f'The number of overlapping pairs is {overlaps}.')

main()