import sys
import re

def main():
    get_score()

def get_score():
    combos = {'AX': 4,
              'AY': 8,
              'AZ': 3,
              'BX': 1,
              'BY': 5,
              'BZ': 9,
              'CX': 7,
              'CY': 2,
              'CZ': 6}
    score = 0

    filename = sys.argv[1]
    f = open(filename, 'r')
    for line in f.readlines():
        pattern = re.compile(r'\s+')
        score += combos[re.sub(pattern, '', line)]
    print(f'The score given by the guide is {score}')

main()