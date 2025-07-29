import random
import math
import sys

print(" ")
print("🧱 ROCK 📄 PAPER ✂ SCISSORS GAME:")
print(" ")

# Playerchoice code
playerchoice = input(
    "\n"
    "1 FOR 🧱ROCK.\n"
    "2 FOR 📄PAPER.\n"
    "3 FOR ✂ SCISSORS.\n"
    "Please enter your number:"
)
player = int(playerchoice)
if player < 0 or player > 3:
    sys.exit("You must enter 1,2,or 3...")
    print(" ")

# pythonchice code
computerchoice = random.choice("123")
computer = int(computerchoice)

# summary
print("👍You chose:" + playerchoice + ".")
print("🐍Python chose:" + computerchoice + ".")
print(" ")

# Gamecondition
if player > computer:
    print("You win 🎉")
elif player < computer:
    print("Python wins 🐍")
else:
    print("TIE GAME😳")
print(" ")
