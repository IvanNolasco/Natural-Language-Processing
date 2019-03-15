import operator
import numpy as np
import math
from raw_freq_vectors import *
from write import writeList
  
def cosine_similarity(raw_freq_vectors_dict, word):
    similar_words_dict={}
    vector_to_compare=raw_freq_vectors_dict[word]
    v_to_compare=np.array(vector_to_compare)
    
    vc_squared=v_to_compare**2
    vc_sum=vc_squared.sum()
    vc_length=math.sqrt(vc_sum) 
    
    i=0
    for key in raw_freq_vectors_dict.keys():
        v=np.array(raw_freq_vectors_dict[key])
        
        v_squared=v**2
        v_sum=v_squared.sum()
        v_length=math.sqrt(v_sum) 
        lengths_product=vc_length*v_length
        
        similar_words_dict[key]=np.dot(v_to_compare, v)/lengths_product        
        i+=1
        print('cosine_similarity function ', str(i), str(similar_words_dict[key]))
    
    similar_words = sorted(similar_words_dict.items(), key=operator.itemgetter(1), reverse=True)
    return similar_words
    
'''test if run as application'''
if __name__=='__main__':
    fname_vocabulary='C:\\Users\\navi_\\Dropbox\\NLP\\Programas\\e960401_vocabulary.txt'    
    fname_contexts='C:\\Users\\navi_\\Dropbox\\NLP\\Programas\\e960401_contexts.txt'
    raw_freq_vectors_dict=raw_freq_vectors(fname_vocabulary, fname_contexts)
    freq_vectors_dict=freq_vectors(raw_freq_vectors_dict)
    word='empresa'
    similar_words=cosine_similarity(raw_freq_vectors_dict, word)
    writeList(similar_words, 'C:\\Users\\navi_\\Dropbox\\NLP\\Programas\\'+word+'_similar_words_without_stopwords.txt')
    similar_words2=cosine_similarity(freq_vectors_dict, word)
    writeList(similar_words2, 'C:\\Users\\navi_\\Dropbox\\NLP\\Programas\\'+word+'_similar_words2_without_stopwords.txt')