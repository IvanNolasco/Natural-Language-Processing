from clean_tokens import *

import math
import nltk
import operator
from write import writeList

def mutual_information(pw1_1,pw2_1,pw1_1w2_1):
    """obtiene la informacion mutua de dos palabras"""
    pw1_0 = 1 - pw1_1
    pw2_0 = 1 - pw2_1
    pw1_1w2_0 = pw1_1 - pw1_1w2_1
    pw1_0w2_0 = pw2_0 - pw1_1w2_0
    pw1_0w2_1 = pw2_1 - pw1_1w2_1
    #Se aplica la formula de informacion mutua
    mutualInformation = (pw1_0w2_0*math.log(pw1_0w2_0/(pw1_0*pw2_0),2))+\
    (pw1_1w2_0*math.log(pw1_1w2_0/(pw1_1*pw2_0),2))+\
    (pw1_0w2_1*math.log(pw1_0w2_1/(pw1_0*pw2_1),2))+\
    (pw1_1w2_1*math.log(pw1_1w2_1/(pw1_1*pw2_1),2))
    return mutualInformation

def smooth_prob_word_in_sentences(w, sentences):
    """obtiene la probabilidad de una palabra en oraciones con smoothing"""
    N = len(sentences)
    freq = 0
    for sent in sentences:
        if w in sent:
            freq += 1
    prob = (freq+0.5)/(N+1)
    return prob

def smooth_prob_conj(w1, w2, sentences):
    """obtiene la probabilidad conjunta de dos palabras con smoothing"""
    N = len(sentences)
    freq = 0
    for sent in sentences:
        if w1 in sent and w2 in sent:
            freq += 1
    prob = (freq+0.25)/(N+1)
    return prob

def getSentences(text):
	"""Obtiene las oraciones de un texto"""
	sent_tok = nltk.data.load('nltk:tokenizers/punkt/english.pickle')
	sentences = sent_tok.tokenize(text)
	return sentences

def mutual_information_of_text(word, sentences, vocabulary):
    """Obtiene la entropia condicional de una palabra con el vocabulario de un texto"""
    pw1 = smooth_prob_word_in_sentences(word, sentences)
    
    mutInfo = {}
    
    for w in vocabulary:
        pw2 = smooth_prob_word_in_sentences(w, sentences)
        pw1w2 = smooth_prob_conj('empresa', w, sentences)
        mi = mutual_information(pw1, pw2, pw1w2)
        mutInfo[w] = mi
    
    return sorted(mutInfo.items(), key= operator.itemgetter(1), reverse=True)
    

if __name__ == '__main__':
    """obteniendo el texto para tokenizar por oraciones"""
    fname='C:\\Users\\navi_\\Dropbox\\NLP\\Corpus\\e960401.htm'
    text_string=get_text_string(fname)
    sentences = getSentences(text_string) 
    #print('No de oraciones: ',len(sentences))
    
    """obteniendo el vocabulario"""
    fname_vocabulary='C:\\Users\\navi_\\Dropbox\\NLP\\Programas\\e960401_vocabulary.txt'
    f_vocabulary=open(fname_vocabulary, encoding='utf-8')
    voc=f_vocabulary.read()
    vocabulary=voc.split()
    f_vocabulary.close()       
    
    """obteniendo la informacion mutua entre empresa y las palabras del vocabulario"""
    mutInfo = mutual_information_of_text('empresa', sentences, vocabulary)
    writeList(mutInfo, 'C:\\Users\\navi_\\Dropbox\\NLP\\Programas\\empresa_mutual_information.txt')