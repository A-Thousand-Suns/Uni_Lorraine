import json
import nltk

path = r'G:\corpus\layer1.json'
with open(path, 'r') as file:
    time = 0
    for line in file:
        print(line)
        time+=1
        if(time == 2):
            line = line[:-2]
            print(line)
            print(type(line))
            dic = json.loads(line)
            print(type(dic))
            ingre = dic["ingredients"]
            print(ingre)
            for i in ingre:
                print(i["text"])
                text = i["text"]


            break