# from sklearn.feature_extraction.text import TfidfVectorizer
# import nltk
# doc1 = "I have a pen"
# doc2 = "I have an apple"
# wordDict = dict.fromkeys((set(doc1.split(' ')).union(doc2.split(' '))), 0)
# for word in ((doc1+' '+doc2).split(' ')):
#     wordDict[word] = wordDict[word]+1
# print(wordDict)
#
# tfA, tfB = dict.fromkeys(wordDict.keys(), 0), dict.fromkeys(wordDict.keys(), 0)
#
# for word in doc1.split(' '):
#     if(word in tfA.keys()):
#         tfA[word] += 1
#
# for i in tfA.keys():
#     tfA[i] = tfA[i]/float((doc1.split(' ')).__len__())
#
# for word in doc2.split(' '):
#     if(word in tfB.keys()):
#         tfB[word] += 1
#
# for i in tfB.keys():
#     tfB[i] = tfB[i]/(doc2.split(' ')).__len__()
#
# print(tfA)
# print(tfB)
#
# from math import sqrt
# #
#
# def sq_root(n):
#     print('The square root of %0.2f is %0.2f'%(float(n), sqrt(float(n))))
#
#
# sq_root(25)
for i in range(2):
    print(i)
s = '| song            |    Style     |'
print(s.__len__())

def hello(a:int):
    '''hello'''
    return a


def autodoc(f):
    # your code here

    print(f.__doc__)
    print(f.__annotations__)

    for key, value in f.__annotations__.items():
        print('....' + key + ': ' + value.__name__)


autodoc(hello)