import sys
def main():
    get_calibration_sum()

def get_calibration_sum():
    print('Reading calibration document...')
    filename = sys.argv[1]
    f = open(filename, "r")
    
    sum_calibration = 0
    for line in f.readlines():
        #method 1: regex to get numbers
        #method 2: simple for loop through characters, check ascii
        for character in line:
            if ord(character) >=  48 and ord(character) <= 57:
                n1 = character
                break
        for i in range(len(line)-1, -1, -1):
            if ord(line[i]) >=  48 and ord(line[i]) <= 57:
                n2 = line[i]
                break

        sum_calibration += int(n1+n2)
    f.close()
    print(f'The calibration sum is {sum_calibration}')

main()