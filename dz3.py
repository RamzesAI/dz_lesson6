class Worker:
    worker_name = 'Ivan'
    worker_surname = 'Pupkin'
    worker_position = 'Manager'
    wage = 10000
    bonus = 5000
    _worker_income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        print(self.worker_name, self.worker_surname)

    def get_total_income(self):
        print(self.wage + self.bonus)

w = Position()
w.get_full_name()
w.get_total_income()