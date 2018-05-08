def decode(words):
    prevList = []
    prevList.append('start')
    viterbi = {}
    viterbi['start', 0] = 1
    backptr = {}
    wordTag = []
    index = 1
    x = None
    backptr = {}
    finalLine = []

    words = line.split()
    for word in words:
        tags = wordAllTag.get(word,distinctTag)
        for tag in tags:
            for prevState in prevList:
                pair = (tag, index)
                pair1 = (word, tag)
                probT = (transition.get((prevState, tag),0) + 1)/ (tagCount[prevState] + len(distinctTag))
                if viterbi.get(pair, -1) < probT * viterbi[prevState, index -1]* emission.get(pair1,1):
                        x = prevState
                        viterbi[tag, index] = probT* viterbi[prevState, index -1]* emission.get(pair1,1)
                        backptr[tag, index] = x
            # print(backptr)
            # wordTag.append(str(words[index -1]) +'/'+x)
        prevList = tags
        index = index +1
    maxP = 0
    for tag in prevList:
        pair = (tag, index -1)
        if viterbi.get(pair, 0) > maxP:
                x = tag
                maxP = viterbi.get(pair, 0)
    backptr['last', index] = x
    currentT = "last"
    # print(backptr)
    prevT = backptr[(currentT, index)]
    while prevT != 'start':
        prevT = backptr[(currentT, index)]
        # print (prev_tag)
        # print (index)
        # print(len(words))
        # wordTag.insert(words[index-1])
        wordTag.insert(0, words[index-2] + "/" + prevT)
        currentT = prevT
        index -= 1
    finalLine = wordTag[1:]
    # print(finalLine)
    return finalLine





import json
import sys
import operator
import io
from math import log10

f = open('hmmmodel.txt', 'r')
l = f.readlines()
f.close

emission = eval(l[0])
transition = eval(l[1])
wordAllTag = eval(l[2])
distinctTag = eval(l[3])
transition = eval(l[4])
tagCount = eval(l[5])



path = sys.argv[1]
f = open(path, 'r', encoding="utf8")
lines = f.readlines()
f.close()

final = []
answer = []


for line in lines:
    final.append(decode(line))

with io.open('hmmoutput.txt', "w+", encoding="utf-8") as f1:
    for line in final:
        f1.write(str(' '.join(line)))
        f1.write('\n')
f1.close()
