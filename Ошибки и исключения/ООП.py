class House():
    # Документирование класса
    """Описание дома"""

    def __init__(self, street, number):
        """Свойства дома"""
        self.street = street
        self.number = number
        self.age = 0

    def build(self):
        """Строить дом"""
        print(f'Дом на улице {self.street} под номером {self.number} - построен!')

    def age_of_house(self, year):
        """Возраст дома"""
        self.age += year


house1 = House("Московская", 20)
house2 = House("Гаврилова", 4)

print(house1.street)

house1.age_of_house(5)
print(house1.age)


class ProspectHouse(House):
    """Дома на проспекте"""
    def __init__(self, prospect, number):
        super().__init__(self, number)
        self.prospect = prospect

prhouse = ProspectHouse('Проспект Ленина', 20)
print(prhouse.prospect)
