from clean_tokens import *

import math
import nltk
import operator
from write import writeList

def cond_entropy(pw1_1,pw2_1,pw1_1w2_1):
    """obtiene la entropia condicional de dos palabras"""
    pw2_0 = 1-pw2_1
    pw1_1w2_0 = pw1_1 - pw1_1w2_1
    pw1_0w2_0 = pw2_0 - pw1_1w2_0
    pw1_0w2_1 = pw2_1 - pw1_1w2_1
    #Se aplica la formula de la entropia condicional
    if pw1_0w2_0>0 and pw1_0w2_1>0 and pw1_1w2_0>0 and pw1_1w2_1>0:
        condEntropy = (pw1_0w2_0*math.log(pw2_0/pw1_0w2_0,2))+\
        (pw1_1w2_0*math.log(pw2_0/pw1_1w2_0,2))+\
        (pw1_0w2_1*math.log(pw2_1/pw1_0w2_1,2))+\
        (pw1_1w2_1*math.log(pw2_1/pw1_1w2_1,2))
    else:
        condEntropy = 0
    return condEntropy

def prob_word_in_sentences(w, sentences):
    """obtiene la probabilidad de una palabra en las oraciones de un texto"""
    N = len(sentences)
    freq = 0
    for sent in sentences:
        if w in sent:
            freq += 1
    prob = freq/N
    return prob

def prob_conj(w1, w2, sentences):
    """obtiene la probabilidad conjunta de dos palabras"""
    N = len(sentences)
    freq = 0
    for sent in sentences:
        if w1 in sent and w2 in sent:
            freq += 1
    prob = freq/N
    return prob

def getSentences(text):
	"""Obtiene las oraciones de un texto"""
	sent_tok = nltk.data.load('nltk:tokenizers/punkt/english.pickle')
	sentences = sent_tok.tokenize(text)
	return sentences

def cond_entropy_of_text(word, sentences, vocabulary):
    """Obtiene la entropia condicional de una palabra con el vocabulario de un texto"""
    pw1 = prob_word_in_sentences(word, sentences)
    
    condEnt = {}
    
    for w in vocabulary:
        pw2 = prob_word_in_sentences(w, sentences)
        pw1w2 = prob_conj('empresa', w, sentences)
        entropy = cond_entropy(pw1, pw2, pw1w2)
        if entropy:
            condEnt[w] = entropy
    
    return sorted(condEnt.items(), key= operator.itemgetter(1))
    

if __name__ == '__main__':
    """obteniendo oraciones del texto"""
    fname='C:\\Users\\navi_\\Dropbox\\NLP\\Corpus\\e960401.htm'
    text_string=get_text_string(fname)
    sentences = getSentences(text_string)    
    print('No de oraciones: ',len(sentences))
    
    """obteniendo el vocabulario"""
    fname_vocabulary='C:\\Users\\navi_\\Dropbox\\NLP\\Programas\\e960401_vocabulary.txt'
    f_vocabulary=open(fname_vocabulary, encoding='utf-8')
    voc=f_vocabulary.read()
    vocabulary=voc.split()
    f_vocabulary.close()    
    
    """obteniendo la entropia condicional de empresa con las palabras del vocabulario"""
    condEnt = cond_entropy_of_text('empresa', sentences, vocabulary)
    writeList(condEnt, 'C:\\Users\\navi_\\Dropbox\\NLP\\Programas\\empresa_condEnt.txt')
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    