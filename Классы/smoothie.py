class Beverage:

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.cost = sum([prices[fruit] for fruit in self.ingredients])
        self.price = self.cost * 2.5

    def get_cost(self):
        return f'${self.cost:.2f}'

    def get_price(self):
        return f'${self.price:.2f}'

    def get_name(self):
        lst = sorted([i.replace('ies', 'y') for i in self.ingredients])
        return f'{" ".join(lst)} {"Fusion" if len(lst) > 1 else "Smoothie"}'

prices = {"Strawberries": 1.5, "Banana": 0.5, "Mango": 2.5,
            "Blueberries": 1, "Raspberries": 1, "Apple": 1.75,
            "Pineapple": 3.5}

b1 = Beverage(["Strawberries"])
print(b1.ingredients)
print(b1.cost)
print(b1.get_price())
print(b1.get_name())

b2 = Beverage(["Raspberries", "Strawberries", "Blueberries"])
print(b2.ingredients)
print(b2.cost)
print(b2.get_price())
print(b2.get_name())
