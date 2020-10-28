from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import numpy as np;

newsGroupTrain = fetch_20newsgroups(subset='train')
print(newsGroupTrain.target[:10]) # [ 7  4  4  1 14 16 13  3  2  4]
print(newsGroupTrain['target'][2])
print('--------------')

categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
trainSet = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)
testSet = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)
print(trainSet['data'].__len__())
print(trainSet['target'].__len__())
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(trainSet.data)
#print(X_train_counts)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print(X_train_tfidf)

clf = MultinomialNB().fit(X_train_tfidf, trainSet.target)
docs_new = ['God is love', 'OpenGL on the GPU is fast']
X_new_counts = count_vect.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)
predicted = clf.predict(X_new_tfidf)
for doc, category in zip(docs_new, predicted):
    print('%r => %s' % (doc, trainSet.target_names[category]))

twenty_test = fetch_20newsgroups(subset='test',categories=categories, shuffle=True, random_state=42)
docs_test = twenty_test.data
X_test_counts = count_vect.transform(docs_test)
X_test_tfidf = tfidf_transformer.transform(X_test_counts)
predicted = clf.predict(X_test_tfidf)
print(metrics.classification_report(twenty_test.target, predicted,target_names=twenty_test.target_names))
print("accurary\t"+str(np.mean(predicted == twenty_test.target)))

print(type(X_train_tfidf))