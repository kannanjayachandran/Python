# counter in python

from collections import Counter

p = "Python can be easy to pick up whether you're a first time programmer or you're experienced with other languages."
print(Counter(p.lower()))

q = dict(Counter(p.lower()))
# removing special characters, whitespaces etc. Dictionary comprehension is used in here.
q = {k: v for k, v in q.items() if k.isalpha()}
print(type(q), q)
