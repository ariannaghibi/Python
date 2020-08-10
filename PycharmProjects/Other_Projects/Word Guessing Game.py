# Give the user three chances to guess the secret word to win or else they lose.

secret_word = "elephant"
guess_count = 0
guess_limit = 3
print("\n")
while guess_count < guess_limit:
    guess_word = input("Guess the secret word: ")
    if guess_word == secret_word:
        print("YOU WIN!")
        break
    guess_count += 1
if guess_count == guess_limit:
    print("YOU LOSE!")

# Alternative Solution
# secret_word = "giraffe"
# guess_word = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
# while guess_word != secret_word and not (out_of_guesses):
#     if guess_count < guess_limit:
#         guess_word = input("Guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
#
# if out_of_guesses:
#     print("YOU LOSE!")
# else:
#     print("YOU WIN!")