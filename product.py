class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.discount = 0

    def __str__(self):
        return f'{self.name}: ${self.price}'


class Sneaker(Product):
    def __init__(self, name, price, shoe_size, brand):
        # super() returns us the parent class instance
        super().__init__(name, price)
        self.shoe_size = shoe_size
        self.brand = brand


class SoccerBall(Product):
    def __init__(self, name, price, material):
        super().__init__(name, price)
        self.material = material

    def __str__(self):
        parent_str = super().__str__()
        return f'{parent_str} WILSOOOOONNNNNNN'


nike_free = Sneaker("nike Free", "100", "10", "Nike")
soccer_ball = SoccerBall("Wilson", "20", "Rubber")
soccer_ball.discount = 10

print(nike_free.name)
print(nike_free.price)
print(nike_free.brand)
print(nike_free.discount)
print(soccer_ball.discount)