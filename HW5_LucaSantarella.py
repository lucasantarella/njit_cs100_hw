"""
Luca Santarella
CS 100 2018S Section 009
HW 05, September 27, 2019
"""

"""
Exercise 1:
"""

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December')

for month in months:
    if month[0] == 'J':
        print(month)

"""
/ Exercise 1
"""


"""
Exercise 2:
"""

for n in range(100):
    if n % 2 == 0 and n % 5 == 0:
        print(n)

"""
/ Exercise 2
"""


"""
Exercise 3:
"""

horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"

for c in horton:
    if c in vowels:
        print(c)

"""
/ Exercise 3
"""
