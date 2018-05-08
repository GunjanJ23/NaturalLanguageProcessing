class Document:
    def __init__(self, text, trueClass):
        self.text = text
        self.wordFreq = self.wordCount()
        self.trueClass = trueClass

    def getText(self):
        return self.text

    def getWordFreq(self):
        return self.wordFreq

    def getTrueClass(self):
        return self.trueClass

    def wordCount(self):
        wordC = {}
        for word in self.text:
            if word not in stopWordList:
                wordC[word] = wordC.get(word, 0) + 1
        return (wordC)


def stopWords(lines):
    wordC = {}
    for line in lines:
        for word in line:
            wordC[word] = wordC.get(word, 0) + 1
    sortedWordC = sorted(wordC.items(), key=operator.itemgetter(1))
    lastWordC = sortedWordC[-70:]
    lastWord = [i[0] for i in lastWordC]
    lastWord = lastWord
    return (lastWord)


def stem_word(word):
    if len(word) < 5:
        return word
    if word.endswith("or"):
        word = word[:-2]
    return word


def wordchange(word):
    word = word.lower()
    bad_chars = '-$?%.*)(/!+'
    rgx = re.compile('[%s]' % bad_chars)
    word = rgx.sub(' ', word).strip()
    word = word.split()
    return word


def trueClass(class1, class2):
    true = []
    if class1 == "True":
        true.append(1)
    else:
        true.append(-1)

    if class2 == "Pos":
        true.append(1)
    else:
        true.append(-1)

    return true


def vanillaPerceptron(d, iteration, weightsClass1Van, weightsClass2Van, biasVan):
    for i in range(20):
        for line in d:
            wordCountLine = line.getWordFreq()
            classLine = line.getTrueClass()
            weightSum1Van = 0
            weightSum2Van = 0
            for word in wordCountLine.keys():
                if word in stopWordList:
                    continue
                if word not in weightsClass1Van:
                    weightsClass1Van[word] = 0
                if word not in weightsClass2Van:
                    weightsClass2Van[word] = 0
                weightSum1Van += weightsClass1Van.get(word, 0) * wordCountLine[word]
                weightSum2Van += weightsClass2Van.get(word, 0) * wordCountLine[word]
            if classLine[0] * (weightSum1Van + biasVan[0]) <= 0:
                for word in wordCountLine.keys():
                    if word not in stopWordList:
                        weightsClass1Van[word] = weightsClass1Van.get(word, 0) + (classLine[0] * wordCountLine[word])
                biasVan[0] = biasVan[0] + classLine[0]
            if classLine[1] * (weightSum2Van + biasVan[1]) <= 0:
                for word in wordCountLine.keys():
                    if word not in stopWordList:
                        weightsClass2Van[word] = weightsClass2Van.get(word, 0) + (classLine[1] * wordCountLine[word])
                biasVan[1] = biasVan[1] + classLine[1]


def averagePerceptron(d, iteration, weightsClass1Avg, weightsClass2Avg, biasAvg):
    c1 = 1
    c2 = 1
    beta1 = 0
    beta2 = 0
    u1 = {}
    u2 = {}
    for i in range(30):
        for line in d:
            wordCountLine = line.getWordFreq()
            classLine = line.getTrueClass()
            weightSum1Avg = 0
            weightSum2Avg = 0

            for word in wordCountLine.keys():
                if word in stopWordList:
                    continue

                if word not in weightsClass1Avg:
                    weightsClass1Avg[word] = 0

                if word not in weightsClass2Avg:
                    weightsClass2Avg[word] = 0

                weightSum1Avg += weightsClass1Avg.get(word, 0) * wordCountLine[word]
                weightSum2Avg += weightsClass2Avg.get(word, 0) * wordCountLine[word]

            if classLine[0] * (weightSum1Avg + biasAvg[0]) <= 0:
                for word in wordCountLine.keys():
                    if word not in stopWordList:
                        weightsClass1Avg[word] = weightsClass1Avg.get(word, 0) + (classLine[0] * wordCountLine[word])
                        u1[word] = u1.get(word, 0) + float(classLine[0] * c1 * wordCountLine[word])
                biasAvg[0] = biasAvg[0] + classLine[0]
                beta1 = beta1 + float(classLine[0] * c1)

            c1 = c1 + 1

            if classLine[1] * (weightSum2Avg + biasAvg[1]) <= 0:
                for word in wordCountLine.keys():
                    if word not in stopWordList:
                        weightsClass2Avg[word] = weightsClass2Avg.get(word, 0) + (classLine[1] * wordCountLine[word])
                        u2[word] = u2.get(word, 0) + float(classLine[1] * c2 * wordCountLine[word])
                biasAvg[1] = biasAvg[1] + classLine[1]
                beta2 = beta2 + float(classLine[1] * c2)

            c2 = c2 + 1

    for word in weightsClass1Avg.keys():
        weightsClass1Avg[word] = weightsClass1Avg.get(word, 0) - (float(1 / c1) * u1.get(word, 0))
    biasAvg[0] = biasAvg[0] - float(1 / c1) * beta1
    for word in weightsClass2Avg.keys():
        weightsClass2Avg[word] = weightsClass2Avg.get(word, 0) - (float(1 / c2) * u2.get(word, 0))
    biasAvg[1] = biasAvg[1] - float(1 / c2) * beta2


import re
import operator
import sys

path = sys.argv[1]
f = open(path)
lines = f.readlines()
f.close()

weightsClass1Avg = {}
weightsClass2Avg = {}
biasAvg = [0, 0]

weightsClass1Van = {}
weightsClass2Van = {}
biasVan = [0, 0]

iterations = 20
alldoc = []
formatted_lines = {}
for line in lines:
    wordList = line.split()
    sentence = [stem_word(word) for word in wordList[3:]]
    formatted_lines[wordList[0]] = (wordchange(' '.join(sentence)))

stopWordList = stopWords(formatted_lines.values())

for line in lines:
    wordList = line.split()
    class1 = wordList[1]
    class2 = wordList[2]
    d = Document(formatted_lines[wordList[0]], trueClass(class1, class2))
    alldoc.append(d)

averagePerceptron(alldoc, iterations, weightsClass1Avg, weightsClass2Avg, biasAvg)
vanillaPerceptron(alldoc, iterations, weightsClass1Van, weightsClass2Van, biasVan)

f1 = open('vanillamodel.txt', 'w+')
f1.write(str(weightsClass1Van))
f1.write('\n')
f1.write(str(weightsClass2Van))
f1.write('\n')
f1.write(str(biasVan))
f1.write('\n')
f1.write(str(stopWordList))
f1.write('\n')

f2 = open('averagedmodel.txt', 'w+')
f2.write(str(weightsClass1Avg))
f2.write('\n')
f2.write(str(weightsClass2Avg))
f2.write('\n')
f2.write(str(biasAvg))
f2.write('\n')
f2.write(str(stopWordList))
f2.write('\n')
