# Play rock/scissors/paper game against bot ten times and display the scores
import random
# Create a list for the bot to choose either of the three options. Then add the user's input to the bot's choice as a string and check if the result is in the win_list.
bot_list = ['rock', 'scissors', 'paper']
win_list = ['rock'+'scissors', 'scissors'+'paper', 'paper'+'rock']
counter = 0
user_score = 0
bot_score = 0
tie_score = 0
print("\nPlease type either 'rock', 'paper', or 'scissors' to try your luck against bot!\n")
while counter < 10:
    user_input = input("Your move: ")
    bot_input = random.choice(bot_list)
    if user_input in bot_list:
        print("Bot move: " + bot_input)
        if user_input + bot_input in win_list:
            print("You Win!")
            user_score += 1
        elif user_input == bot_input:
            print("Tied!")
            tie_score += 1
        else:
            print("You Lose!")
            bot_score += 1
        counter += 1
    else:
        print("Wrong Input!")
        counter += 0


print(f"Results=> You:{user_score}, Bot:{bot_score}, Ties:{tie_score}")
