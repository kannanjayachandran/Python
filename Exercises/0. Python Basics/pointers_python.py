import ctypes

'''
Although we cannot use pointers in python, the ctypes library (core python library) 
provides utilities to work with pointers
'''

a = ctypes.c_long(100)
ptr = ctypes.pointer(a)

print("The value of a: ", a)

print("\nThe pointer of a: ", ptr)

print("\n ", ptr.contents.value)
print("\nThe address is: ", ctypes.addressof(ptr.contents))

ptr.contents.value = 500

print("The value of a: ", a)