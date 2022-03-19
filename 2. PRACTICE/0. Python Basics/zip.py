# zip function takes iterables, and aggregates them into tuples and returns it.
# We can use Zip function to pack or unpack iterables.

languages = ['Python', 'Java', 'C']
versions = (1, 2, 3)

output = zip(languages, versions)
# This would print the location of the object.
print(output)

# Converting iterator into list.
print(list(output))
