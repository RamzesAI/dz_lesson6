class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def car_go(self):
        print('Car started to go')

    def car_stop(self):
        print('Car stopped')

    def car_direction(self):
        print('Car is changing direction')

    def show_speed(self):
        print(f'Car current speed {self.speed}')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print('Speed is to high')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print('Speed is to high')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

the_car = WorkCar(50, 'black', 'mazda', False)
print(the_car.name)
print(the_car.is_police)
the_car.show_speed()

the_car = SportCar(100, 'red', 'toyota', False)
print(the_car.color)
the_car.car_go()
the_car.show_speed()