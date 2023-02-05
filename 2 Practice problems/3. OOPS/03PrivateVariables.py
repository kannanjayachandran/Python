class A:
    __private_var = 100

    def change_private_var(self, key, value):
        if key == 123:
            self.__private_var = value
            print('Key Changed')
        else:
            print('Wrong key')

a = A()

a.change_private_var(1, 1000)
a.change_private_var(123, 1000)
