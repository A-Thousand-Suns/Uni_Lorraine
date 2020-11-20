from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.svm import SVC
import nltk
from sklearn.metrics import accuracy_score, precision_score, recall_score

categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
trainSet = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)
testSet = fetch_20newsgroups(subset='test', categories=categories, shuffle=True, random_state=42)
print(type(trainSet))
print(trainSet.target)
print(trainSet['data'][0])

wordDict = {}
tokenFilter = nltk.tokenize.RegexpTokenizer(r'\w+')
for doc in trainSet['data']:
    docNoPunc = tokenFilter.tokenize(doc.lower())
    print(docNoPunc)
    
    break

vectorizer = TfidfVectorizer()
train_v=vectorizer.fit_transform(trainSet.data)
test_v=vectorizer.transform(testSet.data)
clusteror = KMeans(n_clusters=4).fit_predict(train_v)
plt.show()
print(type(train_v[0]))
print(type(train_v))

classor = SVC()
classor.fit(train_v, trainSet.target)
result = list(classor.predict(test_v))
print(type(testSet.target))
right = 0

for i in range(list(testSet.target).__len__()):

    if result[i]==list(testSet.target)[i]:
        right+=1
    else:
        print(str(i) + ': ' + str(result[i]))

print(right / result.__len__())

# with open(r'E:\编程文件\python\Uni Lorraine\supervisedProject\temp.txt', 'a') as file:
#     file.write(str(result))
#     file.write('\n')
#     file.write(str(list(testSet.target)))

print(precision_score(testSet.target, result,average='micro'))
print(recall_score(testSet.target, result, average='micro'))
print(train_v.shape)
print(test_v.shape)






