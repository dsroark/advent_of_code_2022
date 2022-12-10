#!/usr/bin/env python

import os
import sys

def get_message_start(message, lookback_count):
    start = lookback_count-1
    for i in range(start, len(message)):
        uniq_chars = len(set(message[i-start:i+1]))
        if uniq_chars != lookback_count:
            continue
        elif uniq_chars == lookback_count:
            return i + 1
        else:
            print("No start of message found!")
            sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {os.path.basename(__file__)} FILENAME")
        sys.exit(0)

    filename = sys.argv[1]
    file = open(filename)

    message = file.read().rstrip()
    print(f"Using four characters: {get_message_start(message, 4)}")

if __name__ == '__main__':
    main()
