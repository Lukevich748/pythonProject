class Name:

    def __init__(self, first_name, last_name):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()

    def full_name(self):
        print(f'{self.first_name} {self.last_name}')

    def initials(self):
        print(f'{self.first_name[0]}.{self.last_name[0]}')

person = Name('ArtEm', 'lukEviCh')
person.full_name()
print(person.first_name)
print(person.last_name)
person.initials()
