import time


text = """
        Python is a very popular general-purpose interpreted, interactive, object-oriented, and high-level 
        programming language. Python is dynamically-typed and garbage-collected programming language. It was 
        created by Guido van Rossum during 1985- 1990. Like Perl, Python source code is also available under 
        the GNU General Public License (GPL). Python supports multiple programming paradigms, including Procedural, 
        Object Oriented and Functional programming language. Python design philosophy emphasizes code readability 
        with the use of significant indentation.
"""

for char in text:
    print(char, end='')
    time.sleep(0.1)
