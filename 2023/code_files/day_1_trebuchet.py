import sys
import re 

def main():
    get_calibration_sum_words()

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

def get_calibration_sum_words():
    print('Reading calibration document...')
    filename = sys.argv[1]
    f = open(filename, "r")
    
    sum_calibration = 0

    for line in f.readlines():
        print(line)
        for i in range(0, len(line)):
            n1 = 0
            character = line[i]
            if character.isdigit():
                n1 = character
            elif len(line) > i+3 and line[i:i+3] == "one":
                n1 = '1'
            elif len(line) > i+3 and line[i:i+3] == "two":
                n1 = '2'
            elif len(line) > i+5 and line[i:i+5] == "three":
                n1 = '3'
            elif len(line) > i+4 and line[i:i+4] == "four":
                n1 = '4'
            elif len(line) > i+4 and line[i:i+4] == "five":
                n1 = '5'
            elif len(line) > i+3 and line[i:i+3] == "six":
                n1 = '6'
            elif len(line) > i+5 and line[i:i+5] == "seven":
                n1 = '7'
            elif len(line) > i+5 and line[i:i+5] == "eight":
                n1 = '8'
            elif len(line) > i+4 and line[i:i+4] == "nine":
                n1 = '9'
            if n1 != 0:
                break
            
        for i in range(len(line)-1, -1, -1):
            n2 = 0
            print(line[i:i-3:-1])
            if line[i].isdigit():
                n2 = line[i]
            elif len(line) > i-3 and line[i-3:i] == "one":
                n2 = '1'
            elif len(line) > i-3 and line[i-3:i] == "two":
                n2 = '2'
            elif len(line) > i-5 and line[i-5:i] == "three":
                n2 = '3'
            elif len(line) > i-4 and line[i-4:i] == "four":
                n2 = '4'
            elif len(line) > i-4 and line[i-4:i] == "five":
                n2 = '5'
            elif len(line) > i-3 and line[i-3:i] == "six":
                n2 = '6'
            elif len(line) > i-5 and line[i-5:i] == "seven":
                n2 = '7'
            elif len(line) > i-5 and line[i-5:i] == "eight":
                n2 = '8'
            elif len(line) > i-4 and line[i-4:i] == "nine":
                n2 = '9'
            if n2 != 0:
                break
        print(n1+n2)
        sum_calibration += int(n1+n2)
    f.close()
    print(f'The calibration sum is {sum_calibration}')

main()