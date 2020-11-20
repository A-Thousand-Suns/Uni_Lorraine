from gensim.test.utils import datapath, get_tmpfile
from gensim.scripts.glove2word2vec import glove2word2vec

gloveFile = datapath(r'E:\编程文件\python\Uni Lorraine\supervisedProject\glove\gloveVectors.txt')
tmp_file = get_tmpfile(r"E:\编程文件\python\Uni Lorraine\supervisedProject\glove\test_word2vec.txt")
glove2word2vec(gloveFile, tmp_file)
