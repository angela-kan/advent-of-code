import sys

def main():
    print(f'The first start of packet market is at {detect_packet_marker()}.')
    print(f'The first start of message market is at {detect_message_marker()}.')


def detect_packet_marker():
    filename = sys.argv[1]
    f = open(filename, 'r')
    signal = f.readline()
    
    nums = {}

    for i in range(len(signal)):
        if len(signal[i:i+4]) == len(set(signal[i:i+4])):
            return i+4

def detect_message_marker():
    filename = sys.argv[1]
    f = open(filename, 'r')
    signal = f.readline()
    
    nums = {}

    for i in range(len(signal)):
        if len(signal[i:i+14]) == len(set(signal[i:i+14])):
            return i+14


main()