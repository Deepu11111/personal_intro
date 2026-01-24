import random

secret_no = random.randint(1,10)
print("I am thinking a number between one and ten..")

guess = int(input("Enter your guessing number : "))

if guess == secret_no:
    print("WOW ! you guessed a right number ...")
elif guess > secret_no:
    print("Ohhh no ! this is too high ..")
else:
    print("No NO No , this is very low you guessed..")