import random

feet_in_mile = 5280
meters_in_kilometer = 1000

def get_file_ext(filename):
    return filename[filename.index(".")+1:]

def roll_dice(num):
    return random.randint(1, num)

class Dice:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def roll_both_dice(self):
        first = random.randint(self.num1, 6)
        second = random.randint(self.num2, 6)
        return first, second

def rand_name_pick(members):
    return random.choice(members)
