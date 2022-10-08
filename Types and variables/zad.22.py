import random

print("Enter your number from 1 to 6")
nr=int(input())

print("The computer throws the dice...")
dice1=random.randint(1,6)
print(int(dice1))

print("Did you win?")
print(nr is dice1)