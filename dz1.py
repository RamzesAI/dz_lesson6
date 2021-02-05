import time


class TrafficLight:
    __color = None

    def running(self):
        count_tr = 0
        while count_tr < 10:
            count_tr += 1
            self.__color = 'red'
            print(f'\033[31m {self.__color}')
            time.sleep(7)
            self.__color = 'yellow'
            print(f'\033[33m {self.__color}')
            time.sleep(2)
            self.__color = 'green'
            print(f'\033[32m {self.__color}')
            time.sleep(10)


t = TrafficLight()
t.running()