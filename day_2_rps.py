import sys
import re

def main():
    get_score_correct()

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

def get_score_correct():
    combos = {'AX': 3,
              'AY': 4,
              'AZ': 8,
              'BX': 1,
              'BY': 5,
              'BZ': 9,
              'CX': 2,
              'CY': 6,
              'CZ': 7}
    score = 0

    filename = sys.argv[1]
    f = open(filename, 'r')
    for line in f.readlines():
        pattern = re.compile(r'\s+')
        score += combos[re.sub(pattern, '', line)]
    print(f'The correct score given by the guide is {score}')

main()