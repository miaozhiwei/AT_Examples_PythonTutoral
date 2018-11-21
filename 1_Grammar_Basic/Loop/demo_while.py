import random

num = random.randint(1, 10)

guess = int(input("Enter a number(0 ~ 10) : "))

while guess != num:

    if guess > num:
        print("The number is %d ,Larger than the num. Try again." % guess)
        guess = int(input("Enter a number(0 ~ 10) : "))
    else:
        print("The number is %d ,Smaller than the num. Try again." % guess)
        guess = int(input("Enter a number(0 ~ 10) : "))

print("You did it , the number is %d " % guess)
