def calprob(className, word,wordin_class):
    if word in wordin_class[className]:
            prob = (wordin_class[className][word])/float(prior[className])

    else:
            prob = 1 / float( prior[className])

    return math.log(prob)


def problines(wordin_class, vocab, prior,priorProb,line,lastWords):


        answerClass = []

        initialProbF = math.log(priorProb["Fake"])
        initialProbT = math.log(priorProb["True"])
        initialProbP = math.log(priorProb["Pos"])
        initialProbN = math.log(priorProb["Neg"])
        wordList = line.split()
        answerClass.append(wordList[0])
        sentence = wordList[1:]
            # print(sentence)
        for word in sentence:
            word = word.lower()
            bad_chars = './!*)($-$%?'
            rgx = re.compile('[%s]' % bad_chars)
            word = rgx.sub('', word)
            if word in lastWords:
                continue

            finalProbF = calprob("Fake",word,wordin_class) + initialProbF
            initialProbF = finalProbF


            finalProbT =calprob("True",word,wordin_class) + initialProbT
            initialProbT = finalProbT


            finalProbN =calprob("Neg",word,wordin_class) + initialProbN
            initialProbN = finalProbN


            finalProbP = calprob("Pos",word,wordin_class) + initialProbP
            initialProbP = finalProbP

        if finalProbF > finalProbT:
            answerClass.append("Fake")
        else:
            answerClass.append("True")

        if finalProbP > finalProbN :
            answerClass.append("Pos")
        else:
            answerClass.append("Neg")
        return(answerClass)




import math
import json
import sys
import operator
import io
import re


f = open('nbmodel.txt', 'r')
l = f.readlines()
f.close()

prior = eval(l[0])
priorProb = eval(l[1])
wordClass = eval(l[2])
# wordClassProb = eval(l[3])
vocab = eval(l[3])
lastWords = eval(l[4])

path = sys.argv[1]
f = open(path, 'r')
lines = f.readlines()
f.close()

final = []

for line in lines:
    final.append(problines(wordClass, vocab, prior,priorProb,line,lastWords))
# print(final)

with io.open('nboutput.txt', 'wb') as f1:
    for line in final:
        f1.write(str(' '.join(line)))
        f1.write('\n')
f1.close()
