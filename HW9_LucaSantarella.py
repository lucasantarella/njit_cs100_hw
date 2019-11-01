"""
Luca Santarella
CS 100 2018S Section 009
HW 08, October 22, 2019
"""

"""
Exercise 1:
"""


def file_copy(inFile, outFile):
    inFileHandle = open(inFile, 'r')
    outFileHandle = open(outFile, 'w')
    outFileHandle.write(inFileHandle.read())
    inFileHandle.close()
    outFileHandle.close()


"""
Exercise 2:
"""


def file_stats(inFile):
    with open(inFile, 'r') as f:
        for i, l in enumerate(f):
            pass
        lineCount = i + 1
        content = f.read()
        wordCount = len(content.split())
        charCount = len(content)
        f.close()
    print("lines " + str(lineCount))
    print("words " + str(wordCount))
    print("chars " + str(charCount))


"""
Exercise 3:
"""

import string


def repeat_words(inFile, outFile):
    outFileHandle = open(outFile, 'w');
    with open(inFile, 'r') as f:
        for line in f:
            lineLower = line.lower()
            duplicateWords = []
            for word in lineLower.split():
                word = word.strip(string.punctuation)
                if lineLower.count(word) > 1 and word not in duplicateWords:
                    outFileHandle.write(word + " ")
                    duplicateWords.append(word)
            if len(duplicateWords) > 0:
                outFileHandle.write("\n")
        f.close()
    outFileHandle.close()


repeat_words('catInTheHat.txt', 'catRepWords.txt')
