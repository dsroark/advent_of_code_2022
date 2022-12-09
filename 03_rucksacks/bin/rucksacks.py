#!/usr/bin/env python

import os
import sys
from string import ascii_lowercase as alc
from string import ascii_uppercase as auc

class Rucksack:
    def __init__(self, items):
        self.items = items
        self.item_compartments = self.__split(items)

    def duplicate_item(self):
        duplicates = []
        for index, item in enumerate(self.item_compartments[0]):
            if item in self.item_compartments[1]:
                duplicates.append(item)
        return list(set(duplicates))

    def items_set(self):
        return set(self.items)

    def item_priority(self, custom_letter=None):
        duplicate = self.duplicate_item()
        if len(duplicate) > 1:
            print(f"Multiple duplicates detected: {duplicate} in {self.itemcompartments}!")
            sys.exit(1)
        elif len(duplicate) < 1:
            return 0
        
        if custom_letter:
            letter = custom_letter
        else:
            letter = duplicate[0]

        if letter in alc:
            return alc.index(letter) + 1
        elif letter in auc:
            return auc.index(letter) + 27
        else:
            print(f"{letter} not a valid item (letter)!!")
            sys.exit(1)

    def __split(self, contents):
        return [ contents[:len(contents)//2], contents[len(contents)//2:] ]

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {os.path.basename(__file__)} FILENAME")
        sys.exit(0)

    filename = sys.argv[1]

    with open(filename) as file:
        lines = [line.rstrip() for line in file]

    ## sum of item priorities
    priority_sum = 0
    for line in lines:
        priority_sum += Rucksack(line).item_priority()

    print(f"The sum of misplaced letters is {priority_sum}")

    priority_sum = 0
    common_letters = {}
    ## sum of group priorities
    print("Group priorities time!\n\n\n\n")
    for index, line in enumerate(lines):
        rucksack = Rucksack(line)

        if (index + 1) % 3 == 1:
            common_letters = rucksack.items_set()
        elif (index + 1) % 3 == 2:
            common_letters = rucksack.items_set().intersection(common_letters)
        elif (index + 1) % 3 == 0:
            common_letters = rucksack.items_set().intersection(common_letters)
            if len(common_letters) != 1:
                print(f"Should only be carrying one of the same time per group! Got {common_letters}")
            else:
                priority_sum += rucksack.item_priority(list(common_letters)[0])
            common_letters = {}
    print(priority_sum)
if __name__ == '__main__':
    main()
