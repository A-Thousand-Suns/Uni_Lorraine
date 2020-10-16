import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import brown
#print(brown.categories())
meat = wn.synset('meat.n.01')
print(meat.lexname)