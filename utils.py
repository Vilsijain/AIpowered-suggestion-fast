import os
import random
import gensim

def load_model():
    # model = gensim.models.KeyedVectors.load_word2vec_format('https://api-cosmodomain.s3.ap-south-1.amazonaws.com/pruned.word2vec.txt', binary=False)
    model = gensim.models.KeyedVectors.load('https://api-cosmodomain.s3.ap-south-1.amazonaws.com/finalgog.txt',mmap='r')
    return model 

 
def generate_prepended_strings(word):
    model = load_model()
    result = model.most_similar(positive=word, topn = 20)
    result = [item[0] for item in result]
    response  = []
    for i in random.sample(result,20):
        response.append(word+i)
    return response

 
def generate_appended_strings(word):
    model = load_model()
    result = model.most_similar(positive=word, topn = 20)
    result = [item[0] for item in result]
    response  = []
    for i in random.sample(result,20):
        response.append(i+word)
    return response



def merge_words(word1,word2):
    model = load_model()
    result1 = model.most_similar(positive=word1, topn = 3)
    result2 = model.most_similar(positive=word2, topn = 3)
    result1 = [item[0] for item in result1]
    result2 = [item[0] for item in result2]
    response = []
    for i in random.sample(result1,3):
        for j in random.sample(result2,3):
            response.append(i+j)
    return response

def generate_top_10(word):
    model = load_model()
    result = model.most_similar(positive=[word], topn = 10)
    return result
