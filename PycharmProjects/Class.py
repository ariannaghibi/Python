class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def is_on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False


class Chef:
    def make_chicken(self):
        print("The chef makes a chicken")

    def make_salad(self):
        print("The chef makes a salad")

    def make_special_dish(self):
        print("The chef makes bbq ribs")


class PersianChef(Chef):
    def make_stew(self):
        print("The Persian chef makes a Ghormeh Sabzi")
