class Airplane:
    def __init__(self, make, company, color, altitude):
        self.__make = make
        self.__company = company
        self.__color = color
        self.__altitude = 0

    def set_make(self, make):
        self.__make = make

    def set_company(self, company):
        self.__company = company

    def set_color(self, color):
        self.__color = color

    def set_altitude(self):
        self.__altitude = 0

    def get_make(self):
        return self.__make

    def get_company(self):
        return self.__company

    def get_color(self):
        return self.__color

    def get_altitude(self):
        return self.__altitude

    def display_info(self):
        print('This is a', self.__color, self.__company, self.__make)

    def altitude(self):
        self.__altitude += 2000
        print('The current altitude is: ', self.get_altitude())

    def altitude_reduction(self):
        self.__altitude -= 100
        print('The current altitude after altitude reduction is: ', self.get_altitude())


airplane = Airplane('A220', 'Airbus', 'white', 0)
airplane.display_info()
airplane.altitude()
airplane.altitude_reduction()

