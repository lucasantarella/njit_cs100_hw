"""
Luca Santarella
CS 100 2018S Section 009
HW 03, September 17, 2019
"""

"""
Exercise 1:
"""
grades = ['A', 'A', 'F', 'C', 'D', 'B', 'C', 'D', 'D', 'D', ]

frequency = [grades.count('A'), grades.count('B'), grades.count('C'), grades.count('D'), grades.count('F'), ]

print("Grade Frequencies: ")
print(frequency)

"""
/ Exercise 1:
"""

"""
Exercise 2:
"""

dog_breeds = ['collie', 'sheepdog', 'Chow', 'Chihuahua', ]
herding_dogs = dog_breeds[:3]
tiny_dogs = dog_breeds[3:]

print("Herding Dogs:")
print(herding_dogs)

print("Tiny Dogs:")
print(tiny_dogs)

print("Persian in `dog_breeds`:")
print('Persian' in dog_breeds)
