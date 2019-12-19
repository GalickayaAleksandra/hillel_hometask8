class Ship:
    def __init__(self, type_ship, fleet, crew, country, speed):
        self.__type = type_ship
        self.__fleet = fleet
        self.__crew = crew
        self.__country = country
        self.__speed = speed

    def set_type_ship(self, type_ship):
        self.__type = type_ship

    def set_fleet(self, fleet):
        self.__fleet = fleet

    def set_crew(self, crew):
        self.__crew = crew

    def set_country(self, country):
        self.__country = country

    def set_speed(self, speed):
        self.__speed = speed

    def get_type_ship(self):
        return self.__type

    def get_fleet(self):
        return self.__fleet

    def get_crew(self):
        return self.__crew

    def get_country(self):
        return self.__country

    def get_speed(self):
        return self.__speed

    def display_info(self):
        print('This is a', self.__type)
        print('He leaves from', self.__country)
        print('His crew is', self.__crew, 'people')

    def swim(self):
        self.__speed = 30
        print('Speed', self.__type, self.__speed, 'km / h')

    def stop(self):
        self.__country = 'Canada'
        print(self.__type, 'stopped in ', self.__country)


ship = Ship('Cargo ship', 'Merchant navy', 100, 'America', 30)
ship.display_info()
ship.swim()
ship.stop()
