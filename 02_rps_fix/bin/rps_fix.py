#!/usr/bin/env python3
import os
import sys

debug=1

def rps_match(opponent, player):
    match_score = 0
    result = ""
    base_score = player[0]
    p1 = opponent[1]
    p2 = player[1]
    if p1 == p2:
        result = "draw"
        match_score = 3
    elif p1 == "rock" and p2 == "paper":
        result = "win"
        match_score = 6
    elif p1 == "rock" and p2 == "scissors":
        result = "loss"
        match_score = 0
    elif p1 == "paper" and p2 == "scissors":
        result = "win"
        match_score = 6
    elif p1 == "paper" and p2 == "rock":
        result = "loss"
        match_score = 0
    elif p1 == "scissors" and p2 == "rock":
        result = "win"
        match_score = 6
    elif p1 == "scissors" and p2 == "paper":
        result = "loss"
        match_score = 0
    else:
        print('not a valid match')
        sys.exit(1)

    match_score = match_score + base_score

    if debug == 1:
        print(f"{p1} vs {p2} resulting in {result}. Match Score: {match_score}")

    return match_score

def rps_translate(choice):
    if choice in ["A","X"]:
        return 1, "rock"
    elif choice in ["B", "Y"]:
        return 2, "paper"
    elif choice in ["C", "Z"]:
        return 3, "scissors"
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
        score = score + rps_match(rps_translate(choices[0]), rps_translate(choices[1]))
        if debug == 1:
            print(f"Running score: {score}")

    
    print(f"The final score is {score}")

if __name__ == '__main__':
    main()
