import matplotlib.pyplot as plt

para = ''' Python is a general-purpose interpreted, interactive, object-oriented, and high-level 
programming language. It was created by Guido van Rossum during 1985- 1990. Like Perl, Python source 
code is also available under the GNU General Public License (GPL). This tutorial gives enough understanding 
on Python programming language.
Python is a MUST for students and working professionals to become a great Software Engineer specially when 
they are working in Web Development Domain. I will list down some of the key advantages of learning Python:
'''

counter = {}

for letter in para:
    counter[letter.lower()] = counter.get(letter, 0) + 1

x, y = zip(*counter.items())
plt.bar(x, y)
plt.show()

counter_clean = {}
for key, value in counter.items():
    if key.isalpha():
        counter_clean[key] = value

x, y = zip(*counter_clean.items())

plt.plot(x, y, color='blue', marker='o', linestyle='dotted',
     linewidth=2, markersize=8)
plt.show()

