# -*- coding: utf-8 -*-
import codecs
import math
import string
from snowballstemmer import stemmer
ar_stemmer = stemmer("arabic")


def stemExsit(word, stems, index):  # checks to see if the stem is already in the list of stems
    for x in stems:
        if (x == word):
            index = x
            return True
    index = -1
    return False


def pause():
    wait = input("Enter any key to continue")


index = -1  # declaring index
stems = []  # list of stems
stemsInst = []  # list of stems instances

print("How many texts would you like to enter?")
numOfTexts = int(input())
for w in range(0, numOfTexts):
    print("Please enter the address of the text you would like to enter")
    address = input()

    file = codecs.open(address, "r", "utf-8")  # open file
    text = file.read()  # text is \the file text

    for w in string.punctuation:  # to remove punctuation marks
        text = text.replace(w, "")
    text = ''.join([c for c in text if c not in "1234567890-,،._–.*"])#remove any and all numbers as well other symbols
    text = ''.join([c for c in text if c not in "؟"])#remove ؟
    words = text.split()  # splitting up all words


    for w in words:  # if new stem add place for it, otherwise increment that stem by 1
        currentRoot = ar_stemmer.stemWord(w)
        if stemExsit(currentRoot, stems, index):#if the root has already been added to the list of roots
            stemsInst[index] = stemsInst[index] + 1
        else:
            stems.append(currentRoot)  # add the new root
            stemsInst.append(1)  # add a 1 to the end for the first instance of the new root

    for w in range(0, len(stems)):  # print table of roots and their instances
        print(f"{stems[w]}:{stemsInst[w]}")
    sum = 0
    for w in stemsInst:
        sum = sum + w
    print("Number of stems:", sum)

    # calculating the entropy
    Entropy = 0
    for w in stemsInst:# sum(px log px)
        Entropy = Entropy + (w / sum) * math.log2(w / sum)
    Entropy = Entropy * -1
    print("Entropy:",Entropy,)

    # calculating the redundancy
    Redundancy = 1 - (Entropy / math.log2(sum))# 1 - H/Hmax
    RedundancyPercent = Redundancy * 100
    print("Redundancy:", RedundancyPercent, "%")
    pause()