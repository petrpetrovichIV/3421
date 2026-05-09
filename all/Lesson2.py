import random

class Student:

    def __init__(self, full_name, years):
        self.full_name = full_name
        self.years = years
        self.skills = 1

    def intro(self):
        print(f'I am a student. My name is {self.full_name}.')
        print(f'I am {self.years} years old.')
        print(f'My skills is {self.skills} xp.')

    def grow_up(self):
        self.years += 1

    def study(self):
        print("Studying 📖🧑‍🎓... +1")
        self.skills += 1

    def chill(self):
        print("Chilling 😎... -1")
        self.skills -= 1

mark = Student("Mark Till", 12)
mark.intro()

for day in range(1,365):
    print(f'day {day}')
    choice = random.randint(0,1)
    if choice == 0:
        mark.chill()
    else:
        mark.study()

mark.grow_up()
mark.intro()