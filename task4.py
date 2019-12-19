class Amphicar:
    def __init__(self, car_type, company, year, movement):
        self.__type = car_type
        self.__company = company
        self.__year = year
        self.__movement = movement

    def set_car_type(self, car_type):
        self.__type = car_type

    def set_company(self, company):
        self.__company = company

    def set_year(self, year):
        self.__year = year

    def set_movement(self, movement):
        self.__movement = movement

    def get_car_type(self):
        return self.__type

    def get_company(self):
        return self.__company

    def get_year(self):
        return self.__year

    def get_movement(self):
        return self.__movement

    def display_info(self):
        print('This is amphibian car')
        print('This is a ', self.__type, self.__year,  'year')

    def movement(self):
        self.__movement = 'crawler track'
        print('The car is driving off-road', self.__movement, 'at a speed of 40 km / h')

    def brake(self):
        print(self.__type, 'stopped moving')


car = Amphicar('All-terrain vehicle', 'Amphicar', 1961, 'crawler track')

car.display_info()
car.movement()
car.brake()
