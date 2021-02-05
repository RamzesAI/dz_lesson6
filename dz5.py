class Stationery:
    title = 'Атрибут метода'

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Отрисовка в Pen')

class Pencil(Stationery):
    def draw(self):
        print('Отрисовка в Pencil')

class Handle(Stationery):
    def draw(self):
        print('Отрисовка в Handle')

s = Stationery()
s.draw()
print(s.title)

s_pen = Pen()
s_pen.draw()

s_pencil = Pencil()
s_pencil.draw()

h = Handle()
h.draw()