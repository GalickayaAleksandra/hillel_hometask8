class Car:
    def __init__(self, color, make, speed):
        self.__color = color
        self.__make = make
        self.__speed = 0

    def set_color(self, color):
        self.__color = color

    def set_make(self, make):
        self.__make = make

    def set_speed(self):
        self.__speed = 0

    def get_color(self):
        return self.__color

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed

    def display_info(self):
        print('This is a', self.__color, self.__make)

    def accelerate(self):
        self.__speed += 5
        print('The current speed is: ', self.get_speed())

    def brake(self):
        self.__speed -= 5
        print('The current speed after brake is: ', self.get_speed())


car = Car("Black", 'BMW', 0)
car.display_info()
car.accelerate()
car.accelerate()
car.brake()
car.brake()
