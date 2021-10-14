#  Write a Python program which accepts a sequence of comma-separated numbers
#  from user and generate a list and a tuple with those numbers. (List -> Tuple)

print("Enter the numbers separated by comas : ")
num = input()
List = num.split(",")
Tuple = tuple(List)
print('List: ', List)
print('Tuple: ', Tuple)
