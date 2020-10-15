import pickle
with(open('instr_vocab.pkl', 'rb')) as file:
    data = pickle.load(file)
print(data)
