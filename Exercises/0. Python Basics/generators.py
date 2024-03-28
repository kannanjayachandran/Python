from sys import getsizeof
import time

t1 = time.time()
lis_normal = [x for x in range(50_000)]
t2 = time.time()
sum(lis_normal)
t3 = time.time()
sN = getsizeof(lis_normal)

tc = (t2 - t1) * 1000
ts = (t3 - t2) * 1000

print(f"Size of the list created using list comprehension is : {sN/1000} KB")

print(f"Time taken to create the list: {tc} and time taken to sum is {ts}\n")

t4 = time.time()
lis_gen = (x for x in range(50_000))
t5 = time.time()
sum(lis_gen)
t6 = time.time()
sG = getsizeof(lis_gen)

tc2 = (t5 - t4) * 1000
ts2 = (t6 - t5) * 1000

print(f"Size of the list created using generator is : {sG} Bytes")

print(f"Time taken to create the list using generators: {tc} and time to sum is {ts2}")

square_gen = (x**2 for x in range(5))
print(square_gen)

for i in range(3):
    print(next(square_gen))

for val in square_gen:
    print(val)


"""
Generators are a simple and powerful tool for creating iterators. 
They are written like regular functions but use the yield statement 
whenever they want to return data. Each time next() is called on it, 
the generator resumes where it left off (it remembers all the data values 
and which statement was last executed). An example shows that generators 
can be trivially easy to create: 

Using generators is memory efficient, as it only produces one item at a time, 
but it is also slower than a normal function.
"""
