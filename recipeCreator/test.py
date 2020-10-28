import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import brown
#print(brown.categories())
meat = wn.synset('dry.n.01')
print(meat.hypernyms())
hyper  = lambda s: s.hypernyms()
print(list(meat.closure(hyper)))