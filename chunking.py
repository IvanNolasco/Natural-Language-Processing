# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 15:57:04 2018

@author: navi_
"""
import nltk
import re
import pprint
from prepare_reviews import prepare_articles

def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences  

sent_tag = prepare_articles('C:\\Users\\navi_\\Desktop\\SFU_Spanish_Review_Corpus\\moviles\\')
new_sent_tag = []
#sent_tag = sent_tag[:1]

for s in sent_tag:
    #print(s)
    new_sent = []
    for t in s:
        #print(t)
        if t[1] == None:
            tup = (t[0],'n')
        elif t[0] == 'de':
            tup = (t[0], 'de')
        else:
            tup = t
        new_sent.append(tup)
    #print(new_sent)
    new_sent_tag.append(new_sent)
#print(new_sent_tag)
grammar = "CHUNK: {<n.*><de><n.*>}"
cp = nltk.RegexpParser(grammar)

for s in new_sent_tag:
    result = cp.parse(s)
    """
    for r in result:
        if isinstance(r, nltk.tree.Tree):
            print(r)
    """
    for subtree in result.subtrees():
        if subtree.label() == 'CHUNK':
            print(subtree)
    
sent = 'Los estudiantes de ESCOM ganaron el premio Nobel'
#download the POS tagger
input=open('UnigramTagger_cess_esp.pkl', 'rb')
tagger=load(input)
input.close()
s_tagged=tagger.tag(nltk.word_tokenize(sent))

new_sent_tag = []
#sent_tag = sent_tag[:1]

for t in s_tagged:
    if t[1] == None:
        tup = (t[0],'n')
    else:
        tup = t
    new_sent_tag.append(tup)
#print(new_sent_tag)
grammar = "NP: {<d.+>?<n.+>*<s.+>?<n.*>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(new_sent_tag)
result.draw()
    
#print(result)
#result.draw()