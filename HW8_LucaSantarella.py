"""
Luca Santarella
CS 100 2018S Section 009
HW 08, October 22, 2019
"""

import random

"""
Exercise 1:
"""


def twoWords(wordOneLength, wordTwoLetter):
    while True:
        FirstLength = input(("Please enter a word with " + str(wordOneLength) + " letters"))
        if len(FirstLength) == wordOneLength:
            if (" " in FirstLength) == False:
                break
    while True:
        SecondWFirstLetter = input(("Please enter a word that starts with " + wordTwoLetter))
        if SecondWFirstLetter.upper()[0] == wordTwoLetter.upper()[0]:
            if (" " in SecondWFirstLetter) == False:
                break
    output = [FirstLength, SecondWFirstLetter]
    return output


"""
Exercise 2:
"""


def twoWordsV2(wordOneLength, wordTwoLetter):
    length = False
    letter = False
    while length == False:
        FirstLength = input(("Please enter a word with " + str(wordOneLength) + " letters"))
        if len(FirstLength) == wordOneLength:
            if (" " in FirstLength) == False:
                length = True
    while letter == False:
        SecondWFirstLetter = input(("Please enter a word that starts with " + wordTwoLetter))
        if SecondWFirstLetter.upper()[0] == wordTwoLetter.upper()[0]:
            if (" " in SecondWFirstLetter) == False:
                letter = True
    output = [FirstLength, SecondWFirstLetter]
    return output


"""
Exercise 3:
"""


def enterNewPassword():
    Len = False
    Num = False
    while ((Len == False) or (Num == False)):
        PW = input("Please enter a password with between 8 and 15 characters and that has at least one digit")
        if (len(PW) > 7) and (len(PW) < 16):
            Len = True
            for i in range(9):
                if str(i) in PW:
                    Num = True
                    break
        if ((Len == False) and (Num == False)):
            output = "The length of the password is not within the bounds of 8 and 15, and the password does not contain a number"
            print(output)
        elif Len == False:
            output = "The length of the password is not within the bounds of 8 and 15"
            print(output)
        elif Num == False:
            output = "The password does not contain a number"
            print(output)
        else:
            output = "The desired password works"
            break
    return output


"""
Exercise 4:
"""


def numberGuesser():
    print("Im thinking of a number between 0 and 50. You have five tries to guess it.")
    num = random.randint(0, 50)
    GCount = 1
    Guess = False
    while (Guess == False) and (GCount < 6):
        UserGuess = int(input("Guess " + str(GCount)))
        if UserGuess == num:
            Guess = True
            return ("You are right! I was thinking of " + str(num) + "!")
        elif UserGuess > num:
            print(str(UserGuess) + " is too high")
            GCount = GCount + 1
        elif UserGuess < num:
            print(str(UserGuess) + " is too low")
            GCount = GCount + 1
        if GCount == 6:
            return ("You were wrong all these times. I was thinking of " + str(num) + "!")


print(twoWords(4, "b"))
print(twoWordsV2(4, "b"))
print(enterNewPassword())
print(numberGuesser())
