from abc import ABC, abstractmethod

class A(ABC):

    @abstractmethod
    def empty_method(self):
        pass

class B(A):
    def empty_method(self):
        print('Now this is a method..')


b = B()
b.empty_method()
