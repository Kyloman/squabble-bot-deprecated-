import pyautogui
import copy
import sys
import pyscreeze
import time
from random import random
from random import *

pyautogui.PAUSE = 0.01
pyautogui.FAILSAFE = True

x1 = 835
x2 = 910
x3 = 980
x4 = 1050
x5 = 1130


ybaseheight = 445
yoffset = 75
xoffset = 75

wrongColor = (155, 93, 247)
includedColor = (214, 190, 0)
correctColor = (46, 216, 60)


list_of_lists = []
incorrectLetters = []
includedLetters = []
correctLetters = []
possibleWords = []
doubleLetterPenalizer = []
values = []

guesses = 0

letterFrequency = {
    's': 46,
    'e': 45,
    'a': 40,
    'r': 30,
    'o': 29,
    'i': 28,
    'l': 25,
    't': 24,
    'n': 21,
    'u': 19,
    'd': 18,
    'c': 15,
    'y': 14,
    'p': 14,
    'm': 14,
    'h': 13,
    'g': 11,
    'b': 11,
    'k': 10,
    'f': 8,
    'w': 7,
    'v': 6,
    'z': 2,
    'x': 2,
    'j': 2,
    'q': 1,
}

def typeword(word, guesses):
    pyautogui.write(word)
    pyautogui.press('enter')
    print("Guessing " + word + "... I've used " + str(guesses) + " guesses." )
    pyautogui.sleep(3)
    getResults(word, guesses)


def getResults(word, guesses):
    tempCounter = 0
    values = ""
    for x in range(0,5):
        if (pyautogui.pixelMatchesColor(x1 + (x * xoffset), ybaseheight + (yoffset * guesses), (wrongColor))):
            foundIncorrectLetter(word[x])
            values += str(0)
        elif (pyautogui.pixelMatchesColor(x1 + (x * xoffset), ybaseheight + (yoffset * guesses), (includedColor))):
            foundIncludedLetter(x, word[x])
            values += str(1)
        elif(pyautogui.pixelMatchesColor(x1 + (x * xoffset), ybaseheight + (yoffset * guesses), (correctColor))):
            foundCorrectLetter(x, word[x])
            values += str(2)
            tempCounter += 1
        else:
            print("Tried invalid word...")
            pyautogui.press('backspace')
            pyautogui.press('backspace')
            pyautogui.press('backspace')
            pyautogui.press('backspace')
            pyautogui.press('backspace')
            possibleWords.remove(word)
            guesses -= 1
            findBestNextWord(guesses)


    print("Values = " + values)
    if (tempCounter == 5):
        finishedPuzzle()
    else:
        guesses += 1
        findBestNextWord(guesses)

def triedInvalidWord(guesses):
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    while(not guesses > 5 ):
        pyautogui.write("mommy")
        pyautogui.press('enter')

    reset()

def findBestNextWord(guesses):
    if(guesses > 5):
        finishedPuzzle()
        print("FINISHED PUZZLE")
    elif (len(possibleWords) == 0):
        guesses += 1
        typeword("mommy", guesses)
    else:
        bestword = possibleWords[0]
        bestWordValue = -1000

        for word in possibleWords:
            currValue = 0
            doubleLetterPenalizer.clear()
            for letter in word:
                currValue += letterFrequency[letter]
                if letter in incorrectLetters:
                    currValue - 50
                if letter in correctLetters:
                    currValue - 50
                if letter in includedLetters:
                    currValue - 50
                if letter in doubleLetterPenalizer:
                    currValue -300
                doubleLetterPenalizer.append(letter)

            if currValue > bestWordValue:
                bestword = word
                bestWordValue = currValue
        typeword(bestword, guesses)





def finishedPuzzle():
    print("Finished puzzle.")
    pyautogui.sleep(10)
    reset()
    typeword("crane", 0)


def foundIncorrectLetter(letter):
    removedWords = 0
    if letter in correctLetters:
        return
    if letter in includedLetters:
        return
    for word in possibleWords:
        if letter in word:
            possibleWords.remove(word)
            removedWords += 1
    print(letter + " is incorrect. Removing " + str(removedWords) + str(len(possibleWords)) + " words.")


def foundIncludedLetter(index, letter):
    print(possibleWords)
    if letter not in includedLetters:
        includedLetters.append(letter)
    for word in possibleWords:
        try:
            if word[index] == letter:
                possibleWords.remove(word)
            elif not (word[index] in word):
                possibleWords.remove(word)
        except:
            print("Word = " + word)
            print("Index = " + index)
            print ("Letter = " + letter)


def foundCorrectLetter(index, letter):
    print(possibleWords)
    if letter not in correctLetters:
        correctLetters.append(letter)
    for word in possibleWords:
        try:
            if word[index] != letter:
                possibleWords.remove(word)
        except:
            print("Word = " + word)
            print("Index = " + index)
            print ("Letter = " + letter)


# Coodrinates
# Point(x=830, y=446)
# Point(x=910, y=445)
# Point(x=980, y=445)
# Point(x=1051, y=448)
# Point(x=1130, y=442)

# Wrong letter: 155, 93, 247
# Included Letter: 214, 190, 0
# Correct Letter: 46, 216, 60

def setup():
    a_file = open("squabbleList.txt", "r")
    for line in a_file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        list_of_lists.append(line_list)
    a_file.close()
    # print(list_of_lists)


def reset():
    print("Resetting...")
    incorrectLetters.clear()
    includedLetters.clear()
    correctLetters.clear()
    doubleLetterPenalizer.clear()
    values.clear()
    global possibleWords
    with open("squabbleList.txt") as f:
        possibleWords = f.read().splitlines()

def main():
    while 1==1:
        pyautogui.sleep(2)
        pyautogui.moveTo(2140,579)
        pyautogui.click()
        pyautogui.click(clicks=2)
        pyautogui.sleep(3000)
        pyautogui.moveTo(631, 168)
        pyautogui.click()
        pyautogui.sleep(360)



    #print("HELLO")
    #guesses = 0
    #setup()
    #reset()
    #pyautogui.sleep(2)
    #typeword("crane", guesses)



#Move to 2140, 579 start.bat
#Double click
#Wait 3 minutes for bots to operate.
#Single click 581,118
#Wait 5 minutes for thread cooldown
#Repeat
if __name__ == "__main__":
    main()