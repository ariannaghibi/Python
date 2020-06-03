secret_word = "giraffe"
guess_word = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess_word != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess_word = input("Guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("YOU LOSE!")
else:
    print("YOU WIN!")

#Alternative Solution
secret_word = "elephant"
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess_word = input("Guess: ")
    guess_count += 1
    if guess_word == secret_word:
        print("YOU WIN!")
        break
else:
    print("YOU LOSE!")