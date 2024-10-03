from classes.autopark import Auto_park
from classes.cars import Passengers_car, Truck, Autobus
from classes.history import History, History_rent


if __name__ == '__main__':
    
    stop = False
    auto_park = Auto_park()
    history_rent = History_rent()

    while stop == False:
        print('1 - Добавить машину')
        print('2 - Посмотреть все машины')
        print('3 - Орендовать Легковую машину')
        print('4 - Орендовать грузовик')
        print('5 - Орендовать автобус')
        print('6 - Посмотреть историю аренд')
        print('7 - Выйти')

        action = input('Введите действие: ')

        if action.isdigit():
            action = int(action)
            if action == 1:
                type_car = input('Введите тип машины: ')
                if type_car == 'легковая':
                    mark = input('Введите марку машины: ')
                    model = input('Введите модель машины: ')
                    year_of_production = int(input('Введите год производства машины: '))
                    kilometers = int(input('Введите пробег машины: '))
                    price = int(input('Введите стоимость проката: '))
                    class_comfortable = input('Введите класс комфорта: ')
                    car = Passengers_car(mark, model, year_of_production, kilometers, price, class_comfortable)
                    auto_park.add_passengers_car(car)
                    print('Машина добавлена')

                elif type_car == 'грузовик':
                    mark = input('Введите марку грузовика: ')
                    model = input('Введите модель грузовика: ')
                    year_of_production = int(input('Введите год производства грузовика: '))
                    kilometers = int(input('Введите пробег: '))
                    price = int(input('Введите стоимость проката: '))
                    weight = int(input('Введите вес грузовика: '))
                    type_body = input('Введите тип кузова: ')
                    auto_park.add_truck(Truck(mark,model,year_of_production,kilometers,price,weight,type_body))
                    print('Машина добавлена')

                elif type_car == 'автобус':
                    mark = input('Введите марку автобуса: ')
                    model = input('Введите модель автобуса: ')
                    year_of_production = int(input('Введите год производства автобуса: '))
                    kilometers = int(input('Введите пробег: '))
                    price = int(input('Введите стоимость проката: '))
                    count_seats = int(input('Введите количество посадочных мест: '))
                    purpose = input('Введите предназначение: ')
                    auto_park.add_autobus(Autobus(mark,model,year_of_production,kilometers,price,count_seats,purpose))
                    print('Машина добавлена')
                else:
                    print('Невозможно добавить машину')
                
            elif action == 2:
                
                print('Легковые машины:')
                auto_park.pasangers_info()
                print('Грузовики:')
                auto_park.trucks_info()
                print('Автобусы:')
                auto_park.autobus_info()

            elif action == 3:
                print('Легковые машины:')
                auto_park.pasangers_info()
                rent_mark = input('Введите марку машины: ')
                rent_car = auto_park.get_mark_passengers(rent_mark)
                if rent_car is None:
                    print('Такой машины нет')
                else:
                    name = input('Введите ваше имя: ')
                    days = int(input('На сколько дней вы хотите взять машину на прокат: '))
                    all_price = rent_car.price * days
                    history = History(rent_car, name, all_price, days)
                    history.info()
                    auto_park.rented_passenger_car(rent_car, name)

            elif action == 4:
                print('Грузовики:')
                auto_park.trucks_info()
                rent_mark = input('Введите марку грузовика: ')
                rent_truck = auto_park.get_mark_trucks(rent_mark)
                if rent_truck is None:
                    print('Такой машины нет')
                else:
                    name = input('Введите ваше имя: ')
                    days = int(input('На сколько дней хотите взять грузовик на прокат: '))
                    all_price = rent_truck.price * days
                    history = History(rent_truck, name, all_price, days)
                    history.info()
                    history_rent.add_history(history)
                    auto_park.rented_truck(rent_truck, name)

            elif action == 5:
                print('Автобусы')
                auto_park.autobus_info()
                rent_mark = input('Введите марку автобуса: ')
                rent_autobus = auto_park.get_mark_autobus(rent_mark)
                if rent_autobus is None:
                    print('Такой машины нет')
                else:
                    name = input('Введите ваше имя: ')
                    days = int(input('На сколько дней вы хотите взять автобус на прокат: '))
                    all_price = rent_autobus.price * days
                    history = History(rent_autobus, name, all_price, days)
                    history.info()
                    history_rent.add_history(history)
                    auto_park.rented_autobus(rent_autobus, name)

            elif action == 6:
                history_rent.get_history()
                
            elif action == 7:
                stop = True