import nltk
import re
import numpy as np
from bs4   import BeautifulSoup
from write import writeList
from compare_lists import compare_lists

def get_text_string(fname):
    '''Receives an html file with a Spanish text, deletes html tags, deletes the em-dash character,
    and convert text to lowercase. Returns text as a string.'''
    
    f=open(fname, encoding='latin-1')
    text_string=f.read()
    f.close()

    soup = BeautifulSoup(text_string, 'lxml')
    text_string = soup.get_text()
    text_string = text_string.replace('\x97', ' ')
    text_string=text_string.lower()
    
    print('The text in', fname, 'has', len(text_string), 'characters.\n')
    return text_string

def get_raw_tokens(text_string):
    '''Receives a text string and returns a list of tokens obtained with nltk.word_tokenize(str).'''

    raw_tokens=nltk.Text(nltk.word_tokenize(text_string))
    print('There are', len(raw_tokens), 'raw tokens.\n')
    return raw_tokens

def clean_tokens(raw_tokens):
    '''Receives a list of raw tokens and returns tokens of letters only.'''
    clean_tokens=[]
    for tok in raw_tokens:
        t=[]
        for char in tok: 
            if re.match(r'[a-záéíóúñüA-ZÁÉÍÓÚÑ]', char):#for Spanish alphabet
                t.append(char)
        letterToken=''.join(t)
        if letterToken !='':
            clean_tokens.append(letterToken)
    
    print('There are', len(set(clean_tokens)), 'clean tokens.\n')
    return clean_tokens

def context_word(tokens, w, windowSize):
    context2=[]
    for i in range(len(tokens)):
        if tokens[i]==w:
            for j in range(i-1, i-int(windowSize/2)-1, -1): #left context
                if j >=0: 
                    context2.append(tokens[j])
            try:
                for j in range(i+1, i+(int(windowSize/2+1))): #right context
                    context2.append(tokens[j])
            except IndexError:
                pass
     
    return context2

def remove_stopwords(dirty_tokens):
    '''Receives a list of tokens and remove the stopwords'''
    cont=0
    free_tokens=[]
    for i in range(len(dirty_tokens)):
        if isstopword(dirty_tokens[i]) == False:
            free_tokens.append(dirty_tokens[i])
        else:
            cont+=1
            print('there is a stopword: ',dirty_tokens[i], 'the cont is ', cont)
    return free_tokens

def isstopword(word):
    fname = 'C:\\Users\\navi_\\Dropbox\\NLP\\Programas\\stopwords_es.txt'
    
    f=codecs.open(fname, encoding='UTF-8')
    text_string=f.read()
    f.close()
    tokens=nltk.Text(nltk.word_tokenize(text_string))
    for w in tokens:
        if w == word:
            return True
    return False

def vsm(bag, voc):
    vec=[]   
    for i in range(len(voc)):
        count = 0
        for j in range(len(bag)):
            if voc[i] == bag[j]:
                count=count + 1
        vec.append(count)
    return vec

def cosv(v1, v2):
    prod = (v1 @ v2)
    n1 = np.sqrt(v1 @ v1)
    n2 = np.sqrt(v2 @ v2)
    try:
        res = prod/(n1 * n2)
    except ZeroDivisionError:
        res = "nan"
    return res


if __name__=='__main__':
    fname='C:\\Users\\navi_\\Dropbox\\NLP\\Corpus\\e960401.htm'
    text_string=get_text_string(fname)
    raw_tokens=get_raw_tokens(text_string)
    clean_tokens=clean_tokens(raw_tokens)
    writeList(clean_tokens, 'C:\\Users\\navi_\\Dropbox\\NLP\\Programas\\e960401_clean_tokens.txt')
    
    difference=compare_lists(raw_tokens, clean_tokens)
    writeList(sorted(difference), 'C:\\Users\\navi_\\Dropbox\\NLP\\Programas\\e960401_difference.txt')
    
    """bag_e =  context_word(clean_tokens, 'empresa', 8)
    bag_c =  context_word(clean_tokens, 'compañía', 8)
    bag_a =  context_word(clean_tokens, 'agua', 8)

    voc=set(clean_tokens)

    vectore = np.array(vsm(bag_e, list(voc)))
    vectorc = np.array(vsm(bag_c, list(voc)))
    vectora = np.array(vsm(bag_a, list(voc)))

    simec = cosv(vectore, vectorc) 
    simea = cosv(vectore, vectora)
    simca = cosv(vectorc, vectora)

    print(simec)
    print(simea)
    print(simca)"""
    voc=set(clean_tokens)
    voclist = sorted(list(voc))

    bag_e =  context_word(clean_tokens, 'empresa', 8)
    vectore = np.array(vsm(bag_e, voclist))

    for i in range(len(voclist)):
        bag = context_word(clean_tokens, voclist[i], 8)
        vector = np.array(vsm(bag, voclist))
        sim = cosv(vectore, vector)
        print (voclist[i],sim)

    
