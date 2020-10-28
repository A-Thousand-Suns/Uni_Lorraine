from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
doc1 = "I have a pen"
doc2 = "I have an apple"
wordDict = dict.fromkeys((set(doc1.split(' ')).union(doc2.split(' '))), 0)
for word in ((doc1+' '+doc2).split(' ')):
    wordDict[word] = wordDict[word]+1
print(wordDict)

tfA, tfB = dict.fromkeys(wordDict.keys(), 0), dict.fromkeys(wordDict.keys(), 0)

for word in doc1.split(' '):
    if(word in tfA.keys()):
        tfA[word] += 1

for i in tfA.keys():
    tfA[i] = tfA[i]/float((doc1.split(' ')).__len__())

for word in doc2.split(' '):
    if(word in tfB.keys()):
        tfB[word] += 1

for i in tfB.keys():
    tfB[i] = tfB[i]/(doc2.split(' ')).__len__()

print(tfA)
print(tfB)


