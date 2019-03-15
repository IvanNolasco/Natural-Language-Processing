from write import writeDict
import numpy as np

def raw_freq_vectors(fname_vocabulary, fname_contexts):
    f_vocabulary=open(fname_vocabulary, encoding='utf-8')
    voc=f_vocabulary.read()
    vocabulary=voc.split()
    f_vocabulary.close()
    
    f_contexts=open(fname_contexts, encoding='utf-8')
    contexts=f_contexts.readlines()
    f_contexts.close()
    
    raw_freq_vectors_dict={}
    for context in contexts:
        words=context.split()
        vector=[]
        for voc in vocabulary:
            vector.append(words[1:].count(voc))
        raw_freq_vectors_dict[words[0]]=vector
        print('raw_frequency_vectors function ', str(contexts.index(context)))
    
    return raw_freq_vectors_dict


def freq_vectors(raw_freq_vectors_dict):
    freq_vectors_dict={}
    for key in raw_freq_vectors_dict.keys():
        v = np.array(raw_freq_vectors_dict[key])
        v_sum = v.sum()
        v_new = v/v_sum
        freq_vectors_dict[key]=v_new
        
        print('frequency_vectors function ', ' ',key, ' ', str(v_sum))
    
    return freq_vectors_dict
    

'''test if run as application'''
if __name__=='__main__':
    fname_vocabulary='C:\\Users\\navi_\\Dropbox\\NLP\\Programas\\e960401_vocabulary.txt'    
    fname_contexts='C:\\Users\\navi_\\Dropbox\\NLP\\Programas\\e960401_contexts.txt'
    raw_freq_vectors_dict=raw_freq_vectors(fname_vocabulary, fname_contexts)
    freq_vector_dict=freq_vectors(raw_freq_vectors_dict)
    #writeDict(raw_freq_vectors_dict, 'C:\\Users\\navi_\\Dropbox\\NLP\\Programas\\e960401_raw_freq.txt')  