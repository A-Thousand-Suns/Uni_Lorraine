from sklearn.datasets import fetch_20newsgroups
from gensim.models import KeyedVectors
import nltk
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score

def matrixCreat(dataSet, wordVectors):
    tokenFilter = nltk.tokenize.RegexpTokenizer(r'\w+')
    docVectorSet = np.zeros(shape=(list(dataSet.data).__len__(),50)) #初始化数据集矩阵
    raw = 0
    for doc in dataSet.data:
        docVec = np.array(wordVectors['the']) #初始化文本矩阵
        sentences = nltk.sent_tokenize(doc)
        time = 0
        error = 0
        for cellSen in sentences:
            words = tokenFilter.tokenize(cellSen.lower())

            for cellWor in words:
                try:
                    wordVec = np.array(wordVectors[cellWor])
                    docVec += wordVec
                    time += 1
                except:
                    error += 1

        docVec = docVec - np.array(wordVectors['the'])
        if raw==0:
            print(docVec)
            print(time)
        docVec = [docVec[i]/time for i in range(50)]
        docVectorSet[raw] = docVec
        #print(error)
        if raw==0:
            print(docVec)

        raw += 1

    print(docVectorSet[0])
    return docVectorSet

categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
trainSet = fetch_20newsgroups(subset='train', categories=categories)
testSet = fetch_20newsgroups(subset='test', categories=categories)
filePath = r'E:\编程文件\python\Uni Lorraine\supervisedProject\glove\test_word2vec.txt'
model = KeyedVectors.load_word2vec_format(filePath)
wordVectors = model.wv
vec = wordVectors['you']
print(trainSet.data[1])

trainVecSet = matrixCreat(trainSet, wordVectors)
testVecSet = matrixCreat(testSet, wordVectors)
print(trainVecSet.shape)
print(list(trainSet.target).__len__())
classor = SVC()
classor.fit(trainVecSet, trainSet.target)
result = list(classor.predict(testVecSet))
print(precision_score(testSet.target, result, average='micro'))

