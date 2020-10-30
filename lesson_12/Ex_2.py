from random import randint


class City:
    def __init__(self):
        self.streets = []

    def pave_the_streets(self):
        for i in range(randint(1, 100)):
            self.streets.append(Street(i))

    def get_population(self):
        population = 0
        for street in self.streets:
            print(f"Street №{street.number}")
            for house in street.houses:
                population += house.people
            print(population)
        return population

    def count_streets(self):
        return len(self.streets)


class Street:
    def __init__(self, number):
        self.number = number
        self.houses = []
        self.build_house()

    def build_house(self):
        for i in range(randint(5, 20)):
            self.houses.append(House())


class House:
    def __init__(self):
        self.people = randint(1, 100)


city = City()
city.pave_the_streets()
city.get_population()
