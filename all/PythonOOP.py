import random

class Student:

    def __init__(self, name):
        self.name = name
        self.skills = 5
        self.money = 100

    def intro(self):
        print(f'My name is {self.name}.')

    def rename(self, new_name):
        self.name = new_name

    def study(self):
        self.skills += 0.5
        print('Studying ...🧑‍🎓📖')

    def chill(self):
        self.skills -= 0.25
        self.money -= random.randint(100,600)
        print('Chilling ...😎👍')

    def work(self):
        self.money += 500
        self.skills += 0.1
        print('Working  ...🧑👷')

    def info(self):
        print(f'skills - {self.skills:.2f}')
        print(f'money  - {self.money} ₴')

alex = Student("Alex")
alex.intro()

for day in range(1,366):
    print(f'\n--- day {day} ---')
    # choice = random.randint(0,2)
    choice = random.choice("scw")
    if choice == 'c':
        alex.chill()
    elif choice == 's':
        alex.study()
    else:
        alex.work()

    alex.info()