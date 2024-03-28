class Animal:

    def eating(self):
        print('Eating..')
    
class dog(Animal):

    def bark(self):
        print('Barking...')

tomy = dog()
tomy.bark()
tomy.eating()
