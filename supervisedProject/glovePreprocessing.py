from sklearn.datasets import fetch_20newsgroups
import nltk
categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
trainSet = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)
tokenFilter = nltk.tokenize.RegexpTokenizer(r'\w+')
time = 0
for doc in trainSet.data:
    sentences = nltk.sent_tokenize(doc)
    print(sentences)
    with open(r'E:\编程文件\python\Uni Lorraine\supervisedProject\result.txt', 'a', encoding='utf-8') as file:

        for cellSen in sentences:
                words = tokenFilter.tokenize(cellSen.lower())
                senNoPun = ''
                for cellWor in words:
                    senNoPun += cellWor + ' '
                print(senNoPun)
                file.write((senNoPun + '\n'))
                time += 1
print(time)
