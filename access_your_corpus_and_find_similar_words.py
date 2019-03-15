'''access your own corpus in NLTK 
and find similar words to a given word'''

import nltk
from nltk.corpus import PlaintextCorpusReader

def first_method(fname, word):
    corpus_root='C:\\Users\\OLGA\\Pprog_work\\NLP_2019_1_programs'
    text=PlaintextCorpusReader(corpus_root, '.*', encoding='latin-1')
    print('Filenames:\n', text.fileids()[:5], '\n')
    vocabulary=text.words(fileids=fname)
    print('Tokens with the first_method:\n', vocabulary[:30], '\n')
    print('There are ', len(vocabulary), 'tokens in ', fname)
    print('Palabras similares a ', word, ':')
    vocabulary=nltk.Text(vocabulary)
    vocabulary.similar(word) #this does not work
    
def second_method(fname, word):
    f=open(fname, 'r', encoding='latin-1')
    text=f.read()
    f.close()

    vocabulary=text.split()
    print('Tokens with the second_method: ', vocabulary[:30], '\n')
    print('There are ', len(vocabulary), 'tokens in ', fname)
    
    voc=nltk.Text(vocabulary)
    print('Other vocabulary with the second_method: ', voc[:30], '\n')
    print('There are ', len(voc), 'tokens in ', fname)
    print('Palabras similares a ', word, ':')
    voc.similar(word)
    
def third_method(fname, word):
    f=open(fname, 'r', encoding='latin-1')
    text=f.read()
    f.close()

    vocabulary=nltk.Text(nltk.word_tokenize(text))
    print('Tokens with the third_method :', vocabulary[:30], '\n')
    print('There are ', len(vocabulary), 'tokens in ', fname)
    print('Palabras similares a ', word, ':')
    vocabulary.similar(word)
       
'''test if run as application'''
if __name__=='__main__':
    fname='e960401.html'
    word='empresa'
    #first_method(fname, word)
    #second_method(fname, word)
    third_method(fname, word)