# zip function takes iterables, and aggregates them into tuples and returns it.
# We can use Zip function to pack or unpack iterables.

languages = ["Python", "Java", "C"]
versions = (1, 2, 3)

output = zip(languages, versions)
# This would print the location of the object.
print(output)

# Converting iterator into list.
print(list(output))

myStr1 = "ABCD"
myStr2 = "xy"
myStr3 = zip(myStr1, myStr2)
print(f"Combined string: {list(myStr3)}")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = list(zip(*matrix))
print(transposed)
