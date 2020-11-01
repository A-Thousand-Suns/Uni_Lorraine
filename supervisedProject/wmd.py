import gensim
word2vec_model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
word2vec_model.init_sims(replace=True) # normalizes vectors
distance = word2vec_model.wmdistance("string 1".split(), "string 2".split())  # Compute WMD as normal.