"""
Luca Santarella
CS 100 2018S Section 009
HW 08, November 1, 2019
"""

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']

"""
Exercise 1:
"""

def initialLetterCount(wordList):
    result = dict()
    for word in wordList:
        if word[0] in result:
            result[word[0]] += 1
        else:
            result[word[0]] = 1
    return result

print(initialLetterCount(horton))

"""
Exercise 2:
"""

def initialLetters(wordList):
    result = dict()
    for word in wordList:
        if word[0] in result and word not in result[word[0]]:
            result[word[0]].append(word)
        else:
            result[word[0]] = [word]
    return result

print(initialLetters(horton))

"""
Exercise 3:
"""


def shareALetter(wordList):
    result = dict()
    for key in wordList:
        words = list()
        for word in wordList:
            for char in key:
                if char in word and word not in words:
                    words.append(word)
        result[key] = words
    return result


print(shareALetter(horton))
