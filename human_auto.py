class Human:
    def __init__(self, name='Human'):
        self.name = name


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, *args):
        for passenger in args:
            self.passengers.append(passenger)

    def print_passengers(self):
        if self.passengers != []:
            print(f"Names of {self.brand} passengers")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(F'There a nor passengers in {self.brand}')


nick = Human('Nick')
kate = Human('Kate')
car = Auto("Mercedes")
car.add_passenger(nick)
car.add_passenger(kate)
car.print_passengers()
