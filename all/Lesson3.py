class Human:
    def __init__(self, name):
        self.name = name

mark = Human('Mark')
nick = Human('Nick')

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def show_passengers(self):

        if self.passengers:
            print(f'{self.brand} passengers:')
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f'There are not passengers in the {self.brand}.')

ferrari = Car("Ferrari 812")
ferrari.add_passenger(mark)
ferrari.add_passenger(nick)
ferrari.show_passengers()