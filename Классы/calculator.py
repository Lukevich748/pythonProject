class Calculator:

    def add(self, x, y):
        return print(x + y)

    def subtract(self, x, y):
        return print(x - y)

    def multiply(self, x, y):
        return print(x * y)

    def divide(self, x, y):
        return print(x // y)

c = Calculator()
c.add(10, 5)
c.subtract(10, 5)
c.multiply(10, 5)
c.divide(10, 5)
