
def checkkey(wordin_class ,word):
    if word not in wordin_class["True"]:
        wordin_class["True"][word] = 0
    if word not in wordin_class["Fake"]:
        wordin_class["Fake"][word] = 0
    if word not in wordin_class["Pos"]:
        wordin_class["Pos"][word] = 0
    if word not in wordin_class["Neg"]:
        wordin_class["Neg"][word] = 0





def wordclass(lines):
    # Create count of each word in a class
    wordin_class = {}
    wordin_class["True" ]= {}
    wordin_class["Fake"] = {}
    wordin_class["Pos"] = {}
    wordin_class["Neg"] = {}

    # Create count of word in Fake
    for line in lines:
        wordList = line.split()
        class1 = wordList[1]
        class2 = wordList[2]
        sentence = wordList[3:]
        # print(sentence)
        for word in sentence:
            word = word.lower()
            bad_chars = './!*)($-$%?'
            rgx = re.compile('[%s]' % bad_chars)
            word = rgx.sub('', word)

            checkkey(wordin_class ,word)
            wordin_class[class1][word] += 1
            wordin_class[class2][word] += 1

    for classes, example in wordin_class.items():
        for key in example.keys():
            example[key] +=1

    return (wordin_class)


def vocab(wordClass, prior):
    voc = {}
    voc["True"] = set()
    voc["Fake"] = set()
    voc["Neg"] = set()
    voc["Pos"] = set()
    for i, s in wordClass.items():
        for classes, count in prior.items():
            if i == classes:
                for word, count in s.items():
                    voc[classes].add(word)

    vocab = {}
    for classes, count in prior.items():
        vocab[classes] = len(voc[classes])
    # print(vocab)
    return (vocab)


def wordCount(lines):
    wordC = {}
    for line in lines:
        for pos, word in enumerate(line.split()):
            if pos > 2:
                word = word.lower()
                bad_chars = './!*)($-$%?'
                rgx = re.compile('[%s]' % bad_chars)
                # word = re.sub('^[^\w]|[^\w]$','',word)
                word = rgx.sub('', word)
                wordC[word] = wordC.setdefault(word, 0) + 1
    sortedWordC = sorted(wordC.items(), key=operator.itemgetter(1))
    lastWordC = sortedWordC[-100:]
    lastWord = [i[0] for i in lastWordC]
    return (lastWord)


def priorClass(wordClass):
    p = {}
    for classes, example in wordClass.items():
        p[classes] = sum(wordClass[classes].values())
    return (p)


def prior_prob(prior):
    # Create dictionary of probability of priors
    prior_prob_class = {}
    for feature, value in prior.items():
        if feature == "True":
            prior_prob_class[feature] = prior[feature] / float(prior["True"] + prior["Fake"])

        elif feature == "Fake":
            prior_prob_class[feature] = prior[feature] / float(prior["True"] + prior["Fake"])

        elif feature == "Pos":
            prior_prob_class[feature] = prior[feature] / float(prior["Pos"] + prior["Neg"])

        elif feature == "Neg":
            prior_prob_class[feature] = prior[feature] / float(prior["Pos"] + prior["Neg"])

    # print(prior_prob_class)
    return (prior_prob_class)


import operator
import json
import sys
import numpy as np
import re

# Open file
path = sys.argv[1]
f = open(path)
lines = f.readlines()
f.close()

# prior = prior(lines)
# wordclassProb = wordclass_prob(wordclass,prior)
wordclass = wordclass(lines)
prior = priorClass(wordclass)
priorprob = prior_prob(prior)
v = vocab(wordclass, prior)
wordcount = wordCount(lines)

prior = str(prior)
priorProb = str(priorprob)
wordClass = str(wordclass)
# wordClassProb = str(wordclassProb)
vocab = str(v)
wordcount = str(wordcount)

f1 = open('nbmodel.txt', 'w+')
f1.write(prior)
f1.write('\n')
f1.write(priorProb)
f1.write('\n')
f1.write(wordClass)
f1.write('\n')
# f1.write(wordClassProb)
# f1.write('\n')
f1.write(vocab)
f1.write('\n')
f1.write(wordcount)
f1.write('\n')

f1.close()
