print("    /|")
print("   / |")
print("  /  |")
print(" /___|")

character_name = "john"
character_age = "85"
print("There once was a man named " + character_name.upper() + ".")
print("He was " + character_age + " years old.")
print("He really liked the name " + character_name.capitalize() + ".")
print("But didn't like to be " + character_age + ".")
print("hello\nhow are you")
print(len(character_name) + len(character_age))
print(character_name[2])
print(character_name.index('n'))
print(character_name.replace("john", "tom"))
print("---------------------------------------------------")

my_age = -75
print("He was " + str(my_age) + " years old.")
print(abs(my_age))
print(pow(2, 3))
print(max(4, 6, 9))
print(min(4, 6, 9))
print(round(3.49))
from math import *

print(floor(3.9))
print(ceil(3.1))
print(sqrt(100))
print("---------------------------------------------------")

try:
    # name = input("enter your name: ")
    # age = input("enter your age: ")
    print("my name is " + name + " and I'm " + age)

    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    result = int(num1) + float(num2)
    print(result)
except NameError as err:
    print(err)

print("---------------------------------------------------")
numbers = [40, 8, 8, 8, 50, 23, 42]
friends = ["Kevin", "Tom", "Alyssa", "Oscar", "Toby"]
friends.sort()
print(friends)
numbers.reverse()
print(numbers)
print(friends[0])
print(friends[-1])
print(friends[2:])
print(friends[1:3])
friends.extend(numbers)
print(friends)
friends.append("Martha")
print(friends)
friends.insert(1, "Jax")
print(friends)
friends.remove("Jax")
print(friends)
friends.pop(11)
print(friends)
print(friends.index('Alyssa'))
print(friends[2])
print(friends.count(8))
friends2 = friends.copy()
print(friends2)
print("---------------------------------------------------")


def say_hi(yourname, yourage):
    print("Hello " + yourname + " you are " + str(yourage))


say_hi("Arian", 32)


def cube(num):
    return pow(num, 3)


print(cube(4))

is_male = True
is_tall = False
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not (is_tall):
    print("You are a short male")
elif not (is_male) and is_tall:
    print("You are tall but not a male")
else:
    print("You are neither male or tall")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(2, 5, 9))
print("---------------------------------------------------")

try:
    # num1 = float(input("Enter first number: "))
    # op = input("Enter operator: ")
    # num2 = float(input("Enter second number: "))

    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '*':
        print(num1 * num2)
    elif op == '/':
        print(num1 / num2)
    else:
        print("Invalid operator!")
except NameError as err:
    print(err)
print("---------------------------------------------------")

monthconversion = {
    "Jan": "January",
    2: "February"
}
print(monthconversion.get("Jan"))
print(monthconversion[2])
print(monthconversion.get("Feb", "Invalid Key"))
print("---------------------------------------------------")

i = 1
while i < 3:
    print(i)
    i += 1
print("Done with loop")
print("---------------------------------------------------")

secret_word = "giraffe"
guess_word = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess_word != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        # guess_word = input("Guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("YOU LOSE!")
else:
    print("YOU WIN!")
print("---------------------------------------------------")

for letter in "Arian":
    print(letter)

friends = ["John", "Tony", "Chris"]
for friend in friends:
    print(friend)
for index in range(len(friends)):
    print(friends[index])

print("---------------------------------------------------")


def raise_to_power(base_num, pow_num):
    return base_num ** pow_num


print(raise_to_power(5, 3))


def raise_to_power2(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power2(5, 3))
print("---------------------------------------------------")

number_grid = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9],
               [10]]
print(number_grid[3][0])
for element in number_grid:
    for sub_element in element:
        print(sub_element)
print("---------------------------------------------------")


# word = input("Enter a name: ")
def vowel(word):
    translation = ""
    for letter in word:
        if letter.islower():
            if letter in "aeiou":
                translation = translation + 'g'
            else:
                translation = translation + letter
        elif letter.isupper():
            if letter in "AEIOU":
                translation = translation + 'G'
            else:
                translation = translation + letter
        else:
            translation = translation + letter
    return translation


# print(vowel(word))
print("---------------------------------------------------")

try:
    10 / 1
    # number = int(input("Enter a number: "))
    # print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)
print("---------------------------------------------------")

# r: reads only, r+: reads and writes, w: overwrites  only, w+: writes and reads, a: appends only, a+: appends and reads

employee_file = open("employee file.txt", "r")
print(employee_file.writable())
print(employee_file.readlines()[1])
employee_file.close()
print("---------------------------------------------------")

import useful_tools

print(useful_tools.roll_dice(5))
print("---------------------------------------------------")

from Class import Student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)
print(student1.gpa)
print(student2.is_on_probation)
print(student1.is_on_honor_roll())
print("---------------------------------------------------")

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

from Class import Question

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]


def run_test(questions):
    score = 0
    for question in questions:
        user_answer = input(question.prompt)
        if user_answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(question_prompts)))
# run_test(questions)
print("---------------------------------------------------")

from Class import Chef
from Class import PersianChef

myChef = Chef()
myPersianChef = PersianChef()

myChef.make_chicken()
myPersianChef.make_salad()
myPersianChef.make_stew()
print("---------------------------------------------------")