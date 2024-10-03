from __main__ import *

class History:
    def __init__(self, car, name, price_all, days):
        self._car = car
        self._name = name
        self._price_all = price_all
        self._days = days

    def info(self):
        print(f'{self._name}, машина будет орендована на {self._days} дня, и ее стоимость: {self._price_all}', self._car)

class History_rent:
    def __init__(self):
        self._history = []

    def add_history(self,history):
        self._history.append(history)

    def get_history(self):
        for history in self.history:
            history.info()
