import json
import nltk
from nltk.corpus import wordnet as wn

results = []
path = r'G:\corpus\layer1.json'

with open(path, 'r') as file:
    time = 0

    for line in file:
        time+=1

        if(time != 1):
            line = line[:-2]
            dic = json.loads(line)
            ingredients = dic["ingredients"]
            print(ingredients)
            choises = []
            food = wn.synset('food.n.01')
            choises.append(food)
            seasoning = wn.synset('seasoning.n.01')
            fruit = wn.synset('fruit.n.01')
            vegetable = wn.synset('vegetable.n.01')
            meat = wn.synset('meat.n.01')
            plant = wn.synset('plant.n.01')
            animal = wn.synset('animal.n.01')
            flavour = wn.synset('flavour.n.01')

            for content in ingredients:
                temp = []
                ##print(i["text"])
                text = content["text"]
                tokens = nltk.word_tokenize(text)
                tagged = nltk.pos_tag(tokens)
                #print(tagged)

                for unit in tagged:
                    if(unit[1]=='NN' or unit[1]=='NNP' or unit[1]=='NNS'):
                        try:
                            noun = nltk.stem.PorterStemmer().stem(unit[0].lower())
                            noun = noun.lower()
                            kind = wn.synset(unit[0] + '.n.01')
                            # print(unit[0])
                            # print('food:'+str(food.wup_similarity(kind)))
                            # print('flavour:' + str(flavour.wup_similarity(kind)))
                            # print('plant:'+str(plant.wup_similarity(kind)))
                            # print('animal:'+str(animal.wup_similarity(kind)))
                            # print('seasoning:'+str(seasoning.wup_similarity(kind)))
                            # print('meat:' + str(meat.wup_similarity(kind)))
                            # print('fruit:' + str(fruit.wup_similarity(kind)))
                            # print('vegetable:' + str(vegetable.wup_similarity(kind)))

                            if(food.wup_similarity(kind)>=0.5 or
                            flavour.wup_similarity(kind)>=0.5 or
                            plant.wup_similarity(kind)>=0.5 or
                            animal.wup_similarity(kind)>=0.5 or
                            seasoning.wup_similarity(kind)>=0.5 or
                            meat.wup_similarity(kind)>=0.5 or
                            fruit.wup_similarity(kind)>=0.5 or
                            vegetable.wup_similarity(kind)>=0.5):
                                temp.append(kind)
                        except:
                            continue

            if(temp.__len__() != 0):
                print(temp)
                print('--------------')

