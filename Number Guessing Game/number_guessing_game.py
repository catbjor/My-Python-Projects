import random
lower = int(input("Enter the lower bound: "))
upper = int(input("\nEnter the upper bound: "))
if lower >= upper:
    print('\nUpper bound must be greater that lower bound')
    exit()
num = random.randint(lower, upper)
chances = 3
print(f"\nYou have {chances} chances to guess the number!\n")
count = 0
guessed = False
while count < chances:
    count += 1
    guess = int(input("Guess a number: "))
    if num == guess:
        print("Congratulations, you did it in ", count, "try!")
        guessed = True
        break
    elif num > guess:
        print("You guessed too small.")
    elif num < guess:
        print("You guessed too high.")
if not guessed:
    print("\nThe number is %d" % num)
    print("\nBetter luck next time!")
