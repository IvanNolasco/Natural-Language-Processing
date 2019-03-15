# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 00:58:48 2018

@author: navi_
"""

import nltk
from split_articles import split_into_articles
from condentropy import getSentences
from write import writeList

def get_capital_letter_words(words):
    cap_let_word = ''
    for i in range(len(words)):
        if (' '.join(words[:i+1]).istitle() or ' '.join(words[:i+1]).isupper()) and words[i].isalnum():
            cap_let_word = ' '.join(words[:i+1])
            i += 1
        else:
            break
    if len(words[i:])<2:
        return [cap_let_word]
    else:
        return [cap_let_word] + get_capital_letter_words(words[i+1:])

if __name__=='__main__':
    articles = split_into_articles('C:\\Users\\navi_\\Dropbox\\NLP\\Corpus\\e960401.htm')
    
    sentences = []
    
    for a in articles:
        sents = getSentences(a)
        for s in sents:
            sentences.append(s)

    cl_words = []
    for s in sentences:
        words = nltk.word_tokenize(s)
        cl_words = cl_words + get_capital_letter_words(words)
    cl_words = sorted(set(cl_words))
    
    writeList(cl_words, 'name_entity.txt')
