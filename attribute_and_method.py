class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1:
            print('Такого этажа не существует')
        for i in range(1, new_floor + 1):
            if i > self.number_of_floors:
                print('Такого этажа не существует')
                break
            else:
                print(i)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
print(f'{h1.name}. кол-во этажей: {h1.number_of_floors}')
h1.go_to(5)
print(f'{h2.name}. кол-во этажей: {h2.number_of_floors}')
h2.go_to(10)

