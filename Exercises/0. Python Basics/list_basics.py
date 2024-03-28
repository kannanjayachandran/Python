# Basic operations on list.

# copying list.
one = [1, 34, 32, 19, 29, 3, 90, 89, 60, 80,  20, 90, 10, 90]
one_copy = one[:]

# append()
one.append(100)  # This would add 100 to the last of the list. It is equivalent to
one[len(one):] = [100]

# extend()
one.extend(one_copy)  # This would extend the list by adding all items from the iterable. it is equivalent to
one[len(one):] = one_copy

# insert
one.insert(0, 100)  # This would insert 100 at 0 index.

# remove
one.remove(100)  # This would remove 100 from the list; it would raise an error if 100 is not present.

# pop
one.pop(5)
# Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes
# and returns the last item in the list.

# clear
one.clear()  # Remove all items from the list.

one = one_copy

# count
x = one.count(90)  # Return the number of times 90 appears in the list.
print(x)

# copy()
z = one.copy()
print(z)

# reverse()
one.reverse()
print(one)

# sort()
one.sort()

print(one)

# Printing elements by group of 2
for i in range(8):
    print(one_copy[i])
    print(one_copy[i + 1])
    print()




