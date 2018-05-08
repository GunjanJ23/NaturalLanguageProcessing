import json
import sys
import numpy as np

#Open file
path = sys.argv[1]
f = open(path,encoding="utf8")
lines= f.readlines()
f.close()

#allword stores all word/tag in single list
allword = []

for line in lines:
    words = line.split()
    for word in words:
        allword.append(word)
# print(allword)

#all word tags separately as elements of list
allWT = []
for element in allword:
    combWT = element.rsplit('/',1)
    for separate in combWT:
        allWT.append(separate)
# print(allWT)

#EMISSION PROBABILITIES
#tag stores all tags
tag = []
count = 0
for i in allWT:
    if count % 2 == 1:
        tag.append(i)
    count += 1
# print(tag)

word = []
count = 0
for i in allWT:
    if count %2 == 0:
        word.append(i)
    count+= 1
# print(word)

#countTag stores the tag and their count as a dictionary
countTag = {}
for i in tag:
    countTag[i] = countTag.setdefault(i,0)+1
# print(countTag)

#Word and tag as dictionary with probabilites in wT
emission = {}

wtPair = [(allWT[i],allWT[i+1]) for i in range(0,len(allWT),2)]
for pair in wtPair:
    emission[pair] = emission.setdefault(pair,0)+1
# print(emission)

wordAllTag = {}
distinctTag = set()


for pair in emission:
    if not pair[0] in wordAllTag:
        wordAllTag[pair[0]] = list()
    wordAllTag[pair[0]].append(pair[1])
    distinctTag.add(pair[1])
# print(wordAllTag)
# print(distinctTag)


for x,y in emission:
    for k in countTag:
        if (y == k):
            emission[x,y] = emission[x,y]/ countTag[k]
# print(emission)


#Transition probabilites
#
mylist = []
onlyTag = []
tags = []
final =[]
start = ["start"]
end = ["end"]
mylist = [line.split() for line in lines]
#Append all tags
for line in mylist:
    onlyTag = [word.rsplit('/',1) for word in line]
    final =  [tg[1] for tg in onlyTag]
    final = start + final + end
    tags.append(final)
# print(tags)


#Make Tag Pair
f = []
transition = {}
tagPair = []
for tag in tags:
    combT = [(tag[i],tag[i+1]) for i in range(0,len(tag)-1,1)]
    tagPair.append(combT)
# print(tagPair)

for pair in tagPair:
    for x in pair:
        f.append(x)
# print(f)

for pair in f:
    transition[pair] = transition.setdefault(pair,0)+1
# print(transition)

tagCount = {}
for (x,y),value in transition.items():
    tagCount[x] = tagCount.setdefault(x,0) +value

    # print(x)
# print(tagCount)

transitionProb = {}
for x,y in transition:
    for k in tagCount:
        if (x == k):
            transitionProb[x,y] = transition[x,y]/ tagCount[k]
# print(transitionProb)



# print(distinctTag)
Emission = str(emission)
TransitionProb= str(transitionProb)
wordAllTag = str(wordAllTag)
distinctTag = str(distinctTag)
Transition= str(transition)
tagCount = str(tagCount)


f1 = open('hmmmodel.txt', 'w+')
f1.write(Emission)
f1.write('\n')
f1.write(TransitionProb)
f1.write('\n')
f1.write(wordAllTag)
f1.write('\n')
f1.write(distinctTag)
f1.write('\n')
f1.write(Transition)
f1.write('\n')
f1.write(tagCount)
f1.write('\n')





f1.close()
