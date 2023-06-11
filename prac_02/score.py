"""
Program to determine score status

Initial Pseudocode:

get score

if score < 0 or score > 100:
    then display invalid score message
else if score >= 90:
    then display excellent message
else if score >= 50:
    then display passable message
else:
    then display bad message

Code taken from broken_score.py in prac_01, and refactored into functions
in this program.
"""

import random


def main():
    """Main program"""
    score = float(input("Enter score: "))
    score = determine_score_status(score)
    print(score)
    random_score = determine_score_status(random.randint(0, 100))
    print(random_score)


def determine_score_status(score):
    """Function decides score status from score"""
    if score < 0 or score > 100:
        score = "Invalid score"
    elif score >= 90:
        score = "Excellent"
    elif score >= 50:
        score = "Passable"
    else:
        score = "Bad"
    return score


main()
