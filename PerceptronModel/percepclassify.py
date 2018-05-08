def wordCount(line, stopWordsList):
    wordC = {}
    for word in line:
        if word not in stopWordsList:
            wordC[word] = wordC.get(word, 0) + 1
    return (wordC)

def stem_word(word):
    if len(word) < 5:
        return word
    if word.endswith("or"):
        word = word[:-2]
    return word

def predict(between,line, weightClass1, weightClass2, bias, stopWordsList):
    countofWord = wordCount(line, stopWordsList)
    weightSum = [0, 0]
    for word in countofWord.keys():
        if word in stopWordsList:
            continue

        if word not in weightClass1:
            weightClass1[word] = 0

        if word not in weightClass2:
            weightClass2[word] = 0

        weightSum[0] += weightClass1.get(word, 0) * countofWord[word]
        weightSum[1] += weightClass2.get(word, 0) * countofWord[word]

    if (weightSum[0] + bias[0]) > 0:
        between.append("True")
    else:
        between.append("Fake")

    if (weightSum[1] + bias[1]) > 0:
        between.append("Pos")
    else:
        between.append("Neg")

    return between


def wordchange(word):
    word = word.lower()
    bad_chars = '-$?%.*)(/!+'
    rgx = re.compile('[%s]' % bad_chars)
    word = rgx.sub(' ', word).strip()
    word = word.split()
    return word

import math
import json
import sys
import operator
import io
import re

path = sys.argv[1]
f = open(path, 'r')
l = f.readlines()
f.close()

weightClass1 = eval(l[0])
weightClass2 = eval(l[1])
bias = eval(l[2])
stopWordsList = eval(l[3])

path = sys.argv[2]
f = open(path, 'r')
lines = f.readlines()
f.close()

final = []
for line in lines:
    between = []
    wordList = line.split()
    alphaNumeric = wordList[0]
    sentence = [stem_word(word) for word in wordList[1:]]
    between.append(alphaNumeric)
    sentence = wordchange(' '.join(sentence))
    predict(between,sentence, weightClass1, weightClass2, bias, stopWordsList)
    final.append(between)

thefile = open('percepoutput.txt', 'w')
for item in final:
  thefile.write(' '.join(item))
  thefile.write('\n')
thefile.close()

