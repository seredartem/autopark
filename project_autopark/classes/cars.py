

class Car:
    def __init__(self, mark, model, year_of_production, kilometers, price, rent = False):
        self._mark = mark
        self._model = model
        self._year_of_production = year_of_production
        self._kilometers = kilometers
        self._price = price
        self._rent = rent

    @property
    def mark(self):
        return self._mark

    @property
    def price(self):
        return self._price
        
    @property
    def rent(self):
        return self._rent
    
    @rent.setter
    def rent(self,state):
        self._rent = state
    
    def info(self):
        print(f'Mark: {self._mark} Model: {self._model} Year if production: {self._year_of_production} Kilometers: {self._kilometers} Price: {self._price} Rent: {self._rent}')

class Passengers_car(Car):
    def __init__(self, mark, model, year_of_production, kilometers, price, class_comfortable):
        super().__init__(mark, model, year_of_production, kilometers, price, rent = False)
        self._class_comfortable = class_comfortable

    def info(self):
        super().info()
        print(f'Class: {self._class_comfortable}')

class Truck(Car):
    def __init__(self, mark, model, year_of_production, kilometers, price, weight, type_body):
        super().__init__(mark, model, year_of_production, kilometers, price, rent = False)
        self._weight = weight
        self._type_body = type_body
    
    def info(self):
        super().info()
        print(f'Weight: {self._weight} Type: {self._type_body}')

class Autobus(Car):
    def __init__(self, mark, model, year_of_production, kilometers, price, count_seats, purpose):
        super().__init__(mark, model, year_of_production, kilometers, price, rent = False)
        self._count_seats = count_seats
        self._purpose = purpose

    def info(self):
        super().info()
        print(f'Count seats: {self._count_seats} Purpose: {self._purpose}')

        