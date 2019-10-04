"""
Luca Santarella
CS 100 2018S Section 009
HW 06, October 1, 2019
"""

"""
Exercise 1:
"""


def hasFinalLetter(strList, Letters):
    result = []
    for str in strList:
        if str[-1] in Letters:
            result.append(str)
    return result


""" 
Tests:
"""

strList = ['Apple', 'banana', 'orange', 'kiwi']
Letters = 'ea'
print(hasFinalLetter(strList, Letters))

strList = ['Luca', 'Michael', 'Eva']
Letters = 'l'
print(hasFinalLetter(strList, Letters))

strList = ['NJIT', 'Rutgers', 'ECC']
Letters = 'ae'
print(hasFinalLetter(strList, Letters))

"""
/ Exercise 1
"""

"""
Exercise 1:
"""


def isDivisible(maxInt, twoInts):
    result = []
    for i in range(start=1, stop=maxInt):
        if i % twoInts[0] == 0 or i % twoInts[1] == 0:
            result.append(i)
    return result


maxInt = 10
twoInts = (2, 3)
print(isDivisible(maxInt, twoInts))

maxInt = 20
twoInts = (10, 3)
print(isDivisible(maxInt, twoInts))

maxInt = 50
twoInts = (60, 70)
print(isDivisible(maxInt, twoInts))

"""
/ Exercise 1
"""
