class Pizza:
    order = 0

    def __init__(self,  ingredients):
        self.ingredients = ingredients
        Pizza.order += 1
        self.order_number = Pizza.order

    @classmethod
    def garden_feast(cls):
        return cls(['spinach', 'olives', 'mushroom'])

    @classmethod
    def hawaiian(cls):
        return cls(['ham', 'pineapple'])

    @classmethod
    def meat_festival(cls):
        return cls(['beef', 'meatball', 'bacon'])

p1 = Pizza(['bacon', 'parmesan', 'ham'])
print(p1.order_number)
print(p1.ingredients)
p2 = Pizza.garden_feast()
print(p2.ingredients)
print(p2.order_number)