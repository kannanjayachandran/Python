from collections import Counter


# A counter is a dict subclass for counting iterable objects (Unordered).
c = Counter()
print(f"\nA new, empty counter: {c}")
c = Counter("Hercules")
print(f"\nA new counter from iterable: {c}")
c = Counter({"A": 1, "B": 2, "C": 3})
print(f"\nA new counter from mapping : {c}")
c = Counter(one=10, two=20)
print(f"\nA new counter from keywords arguments: {c}")

c = Counter(['one', 'two', 'three'])
print(f'\n\nNo key error: {c['Four']}')
c['five'] = 0
print(f'\nThis won\'t delete element:  {c}')
del c['five']
print(f'\nThis will delete: {c}')

c = Counter(a=2, b=3, c=0, d=-10)
print(f"The counter is : {c}\n\nUsing elements(): ")
for i in c.elements():
    print(i, end=" ")
print(f"\nSorting using sorted(reverse=True): {sorted(c.elements(), reverse=True)}")

c = Counter("Geralt of Rivia")
print(f"\nMost common : {c.most_common(3)}")

p = """Python can be easy to pick up whether you're a first time programmer or you're
    experienced with other languages."""
print(Counter(p.lower()))

q = dict(Counter(p.lower()))
# removing special characters, whitespaces etc. Dictionary comprehension is used in here.
q = {k: v for k, v in q.items() if k.isalpha()}
print(type(q), q)

bird = "parrot"
count_letter = Counter(bird)
print(count_letter)
