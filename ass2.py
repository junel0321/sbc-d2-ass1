from random import randint

print("Welcome to Bootcamp Lottery!")

# Place your bet number
bet1 = int(input("Enter 1st Coordinate (0-9): "))
bet2 = int(input("Enter 2nd Coordinate (0-9): "))
bet3 = int(input("Enter 3rd Coordinate (0-9): "))

print("Your Bootcamp Coordinates are: ", bet1, bet2, bet3)

# Random winning numbers
r1 = randint(0, 9)
r2 = randint(0, 9)
r3 = randint(0, 9)

print("The Winning Bootcamp Coordinates are: ", r1, r2, r3)

# The result 
if bet1 == r1 and bet2 == r2 and bet3 == r3:
    print("Congratulations, You've hit the Jackpot!")
elif (bet1 == r1 and bet2 == r3 and bet3 == r2) or \
     (bet1 == r2 and bet2 == r1 and bet3 == r3) or \
     (bet1 == r2 and bet2 == r3 and bet3 == r1) or \
     (bet1 == r3 and bet2 == r1 and bet3 == r2) or \
     (bet1 == r3 and bet2 == r2 and bet3 == r1):
    print("Hapit ra gyd You've Partial Win!")
else:
    print("Patad pa basin diay mo daug naka!")
