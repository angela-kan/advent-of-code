import sys

def main():
    print(f'The first start of packet market is at {detect_marker()}.')

def detect_marker():
    filename = sys.argv[1]
    f = open(filename, 'r')
    signal = f.readline()
    
    nums = {}

    for i in range(len(signal)):
        if len(signal[i:i+4]) == len(set(signal[i:i+4])):
            return i+4


main()