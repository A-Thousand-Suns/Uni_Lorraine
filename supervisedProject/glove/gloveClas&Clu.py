from sklearn.datasets import fetch_20newsgroups
from sklearn.cluster import KMeans
from gensim.models import KeyedVectors
import nltk
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score
import math
from sklearn.metrics.cluster import adjusted_rand_score

def NMI(A,B):
    # 样本点数
    total = len(A)
    A_ids = set(A)
    B_ids = set(B)
    # 互信息计算
    MI = 0
    eps = 1.4e-45
    for idA in A_ids:
        for idB in B_ids:
            idAOccur = np.where(A==idA)    # 输出满足条件的元素的下标
            idBOccur = np.where(B==idB)
            idABOccur = np.intersect1d(idAOccur,idBOccur)   # Find the intersection of two arrays.
            px = 1.0*len(idAOccur[0])/total
            py = 1.0*len(idBOccur[0])/total
            pxy = 1.0*len(idABOccur)/total
            MI = MI + pxy*math.log(pxy/(px*py)+eps,2)
    # 标准化互信息
    Hx = 0
    for idA in A_ids:
        idAOccurCount = 1.0*len(np.where(A==idA)[0])
        Hx = Hx - (idAOccurCount/total)*math.log(idAOccurCount/total+eps,2)
        Hy = 0
    for idB in B_ids:
        idBOccurCount = 1.0*len(np.where(B==idB)[0])
        Hy = Hy - (idBOccurCount/total)*math.log(idBOccurCount/total+eps,2)
    MIhat = 2.0*MI/(Hx+Hy)
    return MIhat

def matrixCreat(dataSet, wordVectors):
    tokenFilter = nltk.tokenize.RegexpTokenizer(r'\w+')
    docVectorSet = np.zeros(shape=(list(dataSet.data).__len__(),50)) #初始化数据集矩阵
    raw = 0
    for doc in dataSet.data:
        docVec = np.array(wordVectors['the']) #初始化文本矩阵
        # print(docVec)
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
        docVec = [docVec[i]/time for i in range(50)]
        docVectorSet[raw] = docVec
        raw += 1

    #print(docVectorSet[0])
    return docVectorSet

categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
trainSet = fetch_20newsgroups(subset='train', categories=categories)
testSet = fetch_20newsgroups(subset='test', categories=categories)
filePath = r'E:\编程文件\python\Uni Lorraine\supervisedProject\glove\test_word2vec.txt'
model = KeyedVectors.load_word2vec_format(filePath)
wordVectors = model.wv
trainVecSet = matrixCreat(trainSet, wordVectors)
testVecSet = matrixCreat(testSet, wordVectors)
print('trainVecSet.shape', trainVecSet.shape)
print('testVecSet.shape', testVecSet.shape)
classor = SVC()
classor.fit(trainVecSet, trainSet.target)
result = list(classor.predict(testVecSet))
print(precision_score(testSet.target, result, average='micro'))
print(accuracy_score(testSet.target, result))

'''开始举类'''
km = KMeans(n_clusters=4)
cluster_model = km.fit_predict(trainVecSet)
print(km.labels_)
print(trainSet.target)
print(NMI(km.labels_, trainSet.target))
print(adjusted_rand_score(km.labels_, trainSet.target))




