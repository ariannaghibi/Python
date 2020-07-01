# Let the user guess a number and let him know how close he is to the secret number. Display how many attempts it took to guess it right.

import random

secret_num = random.randint(0, 100)
guess_num = -1
guess_count = 0
print(secret_num)
while guess_num != secret_num:
    try:
        guess_num = int(input("Guess: "))
        guess_count += 1
        if guess_num > secret_num:
            print("Too high!")
        elif guess_num < secret_num:
            print("Too low!")
        else:
            print("You got it!")
    except ValueError:
        print("Only numbers are allowed!")
print("Number if tries: " + str(guess_count))
