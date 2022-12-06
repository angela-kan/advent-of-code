import sys
def main():
    find_max_three_calories()

def find_max_calories():
    print('Finding max calories...')
    filename = sys.argv[1]
    f = open(filename, "r")
    max_calories = 0
    current = 0
    for line in f.readlines():
        if line == '\n':
            if current > max_calories:
                max_calories = current
            current = 0
        else:
            current += int(line.strip())
    f.close()
    print(f'The elf carrying the most calories is carrying {max_calories} calories.')

def find_max_three_calories():
    print('Finding 3 max calories...')
    filename = sys.argv[1]
    f = open(filename, "r")
    max_calories = [0 for i in range(3)]
    current = 0
    for line in f.readlines():
        if line == '\n':
            for i in range(len(max_calories)):
                if current > max_calories[i]:
                    max_calories[i] = current
                    max_calories.sort()
                    break
            current = 0
        else:
            current += int(line.strip())
    f.close()
    print(f'The 3 elves carrying the most calories are carrying {sum(max_calories)} calories in total.')

main()