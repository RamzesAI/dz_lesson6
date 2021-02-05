class Road:
    def __init__(self, length, width, height, weight_1sqr):
        self.length = length
        self.width = width
        self.height = height
        self.weight_1sqr = weight_1sqr

    def weight_r(self):
        return self.length * self.width * self.height * self.weight_1sqr


r = Road(20, 5000, 25, 5)
print(r.weight_r())