# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 18:24:40 2018

@author: navi_
"""

from split_articles import split_into_articles
from mutual_information import getSentences
from clean_tokens import *
from nltk.corpus import cess_esp
from lemma import gen_lemmas
import nltk
import operator

def get_sentences_clean(text):
    """return a list of clean sentences from text"""
    sentences = getSentences(text.lower())
    clean_sentences = []
    for sent in sentences:
        tokens = get_clean_tokens(get_raw_tokens(sent))
        sent_aux = " ".join(tokens)
        clean_sentences.append(sent_aux)
    return clean_sentences

def delete_stopwords_tags(stopwords, tags):    
    tags_without_stopwords=[]
    for tag in tags:
        if tag[0] not in stopwords:
            tags_without_stopwords.append(tag)
    return tags_without_stopwords

def gen_lemmas_tags(archivo):
    f=open(archivo)
    t=f.readline()
    d = {}
    while t != "":
        l = t.split()
        if l != []:
            l[0]=l[0].replace("#","")
            #g.write("%s %s\n" %(l[0],l[-1]))
            key = l[0] + ' ' + l[-2].lower()
            d.setdefault(key,l[-1])
        t=f.readline()
    f.close()
    return d

def lemmas_tags_text(lemmas_dict, tags):
    lemmas_tags_text=[]
    for tag in tags:
        key = tag[0] + ' ' + str(tag[1]).lower() #se construye la llave token_etiqueta
        #se busca el lemma de la palabra en el diccionario
        lemma = lemmas_dict.get(key)
        #si se encontro el lemma y no está en la lista se agrega el lemma
        if lemma != None and lemmas_tags_text.count((lemma,tag[1]))==0:
            lemmas_tags_text.append((lemma,tag[1]))
            #sino se encontro se agrega la etiqueta de la palabra 
        elif lemma == None and lemmas_tags_text.count(tag)==0:
            lemmas_tags_text.append(tag)
    return lemmas_tags_text

def get_nouns(lemmas_tags):
    """obtiene los sustantivos de una lista de lemmas"""
    nouns = []
    for lemma in lemmas_tags:
        """si la etiqueta es None porque no tiene lemma o es un sustantivo"""
        if lemma[1] == None or lemma[1][0] == 'n':
            """se agrega solamente el lemma"""
            nouns.append(lemma[0])
    return nouns

def replace_lemmas(lemmas_dict, tokens):
    """remplaza los tokens de un texto por su lemma"""
    lemmas_text = []
    i=0
    for i in range(len(tokens)):
        #se busca el lemma de la palabra en el diccionario
        lemma = lemmas_dict.get(tokens[i])
        #si se encontro el lemma se remplaza el token por el lemma
        if lemma != None :
            lemmas_text.append(lemma)
        #si no se encuentra se escribe el mismo token
        else:
            lemmas_text.append(tokens[i])
    i += 1
    return lemmas_text

if __name__ == '__main__':
    """obtenemos una lista de articulos del texto, sin etiquetas html"""
    texto = 'C:\\Users\\navi_\\Dropbox\\NLP\\Corpus\\e960401.htm'
    articles=split_into_articles(texto)[1:]
    print(articles)
    clean_articles = [] #lista de los articulos dividio en tokens
    """de cada articulo dividimos en oraciones, y a su vez cada oracion dividimos en tokens"""
    tok_sent_art = [] #articulos dividido en oraciones divididas en tokens
    sent_art=[] #articulos dividio en oraciones
    
    for article in articles:
        clean_articles.append(get_clean_tokens(get_raw_tokens(article.lower()))) #crea una lista de los articulos dividio en tokens
        clean_sent = get_sentences_clean(article)
        sent_art.append(clean_sent)
        tok_sent = []
        for sent in clean_sent:
            tok_sent.append(sent.split()) #separa cada oracion en tokens y los mete dentro de una lista
        tok_sent_art.append(tok_sent)
    #print(tok_sent_art)
    #print(sent_art)
    
    """para lematizar"""
    fname_lemmas='C:\\Users\\navi_\\Dropbox\\NLP\\Programas\\generate.txt'
    lemmas_text_dict=gen_lemmas_tags(fname_lemmas)
    lemmas_dict=gen_lemmas(fname_lemmas)
    
    """entrenando el tagger para el etiquetado"""
    cess_tagged_sents=cess_esp.tagged_sents()
    tagger=nltk.UnigramTagger(cess_tagged_sents)
    
    """para eliminar las stopwords"""
    f=open('C:\\Users\\navi_\\Dropbox\\NLP\\stopwords_es.txt', encoding='utf-8')
    words=f.read()
    stopwords=words.split()
    f.close()
    
    tags_sents_arts = [] #etiquetas en cada oracion de cada articulo
    lemmas_tags_art = []
    lemmas_tags_art_aux = [] #lista auxiliar con etiquetas por cada articulo del texto
    newlist = []
    for art in sent_art:
        tags_art = []
        lemmas_tags_aux = [] #lista auxiliar con etiquetas de un articulo sin dividir en oraciones
        
        for sent in art:
            """para etiquetar oraciones"""
            tokens=nltk.word_tokenize(sent)
            s_tagged=tagger.tag(tokens)     #se obtienen las etiquetas de una oracion
            """se eliminan stopwords de las palabras ya etiquetadas"""
            tags = delete_stopwords_tags(stopwords,s_tagged)
            tags_art.append(tags)   #se agrega a la lista de oraciones por articulo
            lemmas_tags_aux.extend(tags) #se crea una lista con todas las etiquetas de un articulo sin dividir en oraciones
        """se lemmatizan las palabras etiquetadas de cada articulo"""
        lemmas_tags_art_aux.append(lemmas_tags_aux)
        lemmas_tags=lemmas_tags_text(lemmas_text_dict, lemmas_tags_aux)
        lemmas_tags_art.append(lemmas_tags) #se agregan a la lista de lemmas de cada articulo
        tags_sents_arts.append(tags_art) #se agrega a la lista de articulos de todo el texto
        
    """obteniendo los sustantivos de cada articulo"""
    nouns_art_list = []
    for art in lemmas_tags_art:
        nouns = get_nouns(art)
        nouns_art_list.append(nouns)
        #print(nouns)
    #writeList(sorted(nouns_art_list), 'C:\\Users\\navi_\\Dropbox\\NLP\\Programas\\e960401_nouns_by_article.txt')
    
    """obteniendo la frecuencia de los sustantivos en cada articulo"""
    nouns_frq_list = []
    i=0
    for art in nouns_art_list:
        nouns_frq_dict = {}
        """se obtiene el articulo remplazando los tokens por su lemma"""
        article_lemmas = replace_lemmas(lemmas_dict, clean_articles[i])
        for noun in art:
            nouns_frq_dict[noun] = article_lemmas.count(noun)
        i += 1
        nouns_frq_list.append(sorted(nouns_frq_dict.items(), key=operator.itemgetter(1), reverse=True))
    #print(nouns_frq_list)
    #writeList(nouns_frq_list, 'C:\\Users\\navi_\\Dropbox\\NLP\\Programas\\e960401_nouns_frq_by_article.txt')