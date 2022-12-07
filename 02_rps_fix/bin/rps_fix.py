#!/usr/bin/env python3
import os
import sys

debug=0

class Choice:
    def __init__(self, name, beats, loses_to, points):
        self.win = 6
        self.draw = 3
        self.loss = 0
        self.name = name
        self.beats = beats
        self.loses_to = loses_to
        self.points = points

    def versus(self, opp_choice):
        if opp_choice == self.beats:
            return self.win
        elif opp_choice == self.loses_to:
            return self.loss
        elif opp_choice == self.name:
            return self.draw
        else:
            print(f"{opp_choice} not a valid choice")
            sys.exit(1)

    # note that the second return value is from the perspective of the class's player
    # and is inverse to the result
    def fix(self, fixed_result):
        if fixed_result in ["Z", "win"]:
            return self.win, self.loses_to
        if fixed_result in ["Y", "draw"]:
            return self.draw, self.name
        if fixed_result in ["X", "loss"]:
            return self.loss, self.beats
        if fixed_result == "fair game":
            return
        else:
            print("Not a valid result")
            sys.exit(1)


def rps_factory(choice):
    if choice in ["rock", "A","X"]:
        return Choice(name="rock", beats="scissors", loses_to="paper", points=1)
    elif choice in ["paper", "B", "Y"]:
        return Choice(name="paper", beats="rock", loses_to="scissors", points=2)
    elif choice in ["scissors", "C", "Z"]:
        return Choice(name="scissors", beats="paper", loses_to="rock", points=3)
    else:
        return "Not a valid choice!"


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {os.path.basename(__file__)} FILENAME")
        sys.exit(0)

    filename = sys.argv[1]

    with open(filename) as file:
        lines = [line.rstrip() for line in file]

    score = 0
    for line in lines:
        choices = line.split()
        them = rps_factory(choices[0])
        me = rps_factory(choices[1])
        score = score + me.versus(them.name) + me.points
        if debug == 1:
            print(f"Running score: {score}")
    print(f"The final score is {score}")

    print("\n\n---------------------\nTHE FIX IS IN!!!\n\n")
    score = 0
    for line in lines:
        choices = line.split()
        them = rps_factory(choices[0])
        the_fix = them.fix(choices[1])
        me = rps_factory(the_fix[1])

        score = score + the_fix[0] + me.points
        if debug == 1:
            print(f"Running score: {score}")

    print(f"The fixed score is {score}")

    

if __name__ == '__main__':
    main()
    
