# Max Susman
# CS 1400 - L01
# Assignment 3

import random

# generates a random integer between 1 and 10
guessNum = random.randint(1, 10)

# prompts user for input
pickNum = int(input("What number do you choose (1-10):"))

# msg will store programs response to user input
msg = ""

# that sweet sweet conditional logic
if guessNum == pickNum:
    msg = "Honored to play with you, Master."
elif pickNum == guessNum + 1 or pickNum == guessNum - 1:
    msg = "You are a worthy opponent, Knight."
elif pickNum == guessNum + 2 or pickNum == guessNum - 2:
    msg = "You have much to learn, Padawan."
elif pickNum == guessNum + 3 or pickNum == guessNum - 3:
    msg = "Youngling, your time will come."
else:
    msg = "Keep working hard in the Service Corps."

# programs response is dislplayed
print(msg)