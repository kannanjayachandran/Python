# creating a class 
class Person:
    is_alive = True
    age = 0

    def __init__(self, age, is_alive) :
        self.age = age
        self.is_alive = is_alive

    def set_name(self, name):
        print(f'You are {name}, and You are {self.age} years old.')

    def is_ghost(self):
        if self.is_alive:
            print('You are not a ghost.')
        else:
            print('You are a 👻')

man1 = Person(19, True)
print('Man1\n')
man1.set_name('King Kong')
man1.is_ghost()

man2 = Person(90, False)
print('\nMan2\n')
man2.set_name('GodZilla')
man2.is_ghost()
