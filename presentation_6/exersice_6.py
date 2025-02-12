class Thing:
    pass

# Выводим класс
print(Thing)


example = Thing()
print(example)

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(f"Name: {self.name}, Symbol: {self.symbol}, Number: {self.number}")


hydrogen = Element('Hydrogen', 'H', 1)
hydrogen.dump()