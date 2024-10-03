
class Auto_park:
    def __init__(self):
        self._passengers_cars = []
        self._trucks = []
        self._autobus = []
        self._rent_cars = []
            
    def pasangers_info(self):
        for car in self._passengers_cars:
            car.info()

    def trucks_info(self):
        for car in self._trucks:
            car.info()

    def autobus_info(self):
        for car in self._autobus:
            car.info()
    
    def add_passengers_car(self,car):
        self._passengers_cars.append(car)   

    def add_truck(self,truck):
        self._trucks.append(truck)

    def add_autobus(self,autobus):
        self._autobus.append(autobus)

    def get_mark_passengers(self,mark):
        for car in self._passengers_cars:
            if car.mark == mark:
                return car
        return None
    
    def get_mark_trucks(self,mark):
        for car in self._trucks:
            if car.mark == mark:
                return car
        return None
    
    def get_mark_autobus(self,mark):
        for car in self._autobus:
            if car.mark == mark:
                return car
        return None

    def rented_passenger_car(self, rent_car):
        rent_car.rent = True
        self._rent_cars.append(rent_car)
        

    def rented_truck(self, rent_truck):
        rent_truck.rent = True

        self._rent_cars.append(rent_truck)

    def rented_autobus(self, rent_autobus):
        rent_autobus.rent = True
        self._rent_cars.append(rent_autobus)

    def get_rent_cars(self):
        for car in self._rent_cars:
            car.info()
