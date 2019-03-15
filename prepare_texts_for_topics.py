import nltk
import re
from pickle import dump, load
from nombre_archivos import get_files_name
from prepareData_Cine import clean_lemma

def prepare_texts(path):
    reviews=[]
    names = get_files_name(path, '.txt')
    #print(names)
    for n in names:
        f = open(path+n)
        text = f.read()
        reviews.append(text)
        
    
    #download the POS tagger
    input=open('UnigramTagger_cess_esp.pkl', 'rb')
    tagger=load(input)
    input.close()
    
    #POS tag reviews
    reviews_tagged=[]
    for r in reviews:
        #get a list of sentences
        sent_tokenizer=nltk.data.load('nltk:tokenizers/punkt/english.pickle')
        sentences=sent_tokenizer.tokenize(r.lower())
        #print(sentences[0])
        
        #tag sentences, a tagged sentence is a list of tuples,
        #each tuple includes 2 elements
        sentences_tagged=[]
        for s in sentences:
            s_tagged=tagger.tag(nltk.word_tokenize(s))
            sentences_tagged.append(s_tagged)
        reviews_tagged.append(sentences_tagged)
        
    #print('\nThis is the first review tagged: \n', reviews_tagged)
    #print(articles_tagged[0][0])
    #print(articles_tagged[0][1]) #print one tagged sentences
    #print(articles_tagged[0][1][0]) #print one tagged word in a sentence
    
    
    with open('stopwords_es.txt', encoding='utf-8') as f:
        stopwords=f.readlines()
        stopwords=[w.strip() for w in stopwords]
    #print(stopwords[:10])
    
    #remove stopwords   
    reviews_without_stopwords=[]
    for r in reviews_tagged: 
        r_clean=[]
        for sentence in r:
            sentence_clean=[]
            for word_tagged in sentence:
                if word_tagged[0] not in stopwords:
                    sentence_clean.append(word_tagged)
            a_clean.append(sentence_clean)
        reviews_without_stopwords.append(a_clean)
    #print('\nThis is the first article without stopwords: \n', articles_without_stopwords)
    
    
    #remove words containing symbols other than letters    
    reviews_without_symbols=[]
    for a in articles_without_stopwords:
        a_clean=[]
        for sentence in a:
            sentence_clean=[]
            for word_tagged in sentence:
                word_list=list(word_tagged)
                w=[]
                for char in word_list[0]: 
                    if re.match(r'[a-záéíóúñü]', char):#for Spanish alphabet
                        w.append(char)
                word_clean=''.join(w)
                if word_clean !='':
                    word_tagged=(word_clean, word_list[1])
                    sentence_clean.append(word_tagged)
            a_clean.append(sentence_clean)
        articles_without_symbols.append(a_clean)
    #print('\nThis is the first article without symbols: \n', articles_without_symbols)
    
    #lemmatize
    input=open('lemmas.pkl', 'rb')
    lemmas=load(input)
    input.close()
                   
    articles_lemmatized=[]
    for a in reviews_without_stopwords:
        a_lemmatized=[]
        for sentence in a:
            sentence_lemmatized=[]
            for word_tagged in sentence:
                if word_tagged[1]==None or word_tagged[1][0]=='F':
                    sentence_lemmatized.append(word_tagged[0])
                else:
                    if word_tagged in lemmas.keys():
                        lemma=lemmas[word_tagged]
                        sentence_lemmatized.append(lemma)
                    else:
                        sentence_lemmatized.append(word_tagged[0])
            a_lemmatized.append(sentence_lemmatized)
        articles_lemmatized.append(a_lemmatized)
    #print('\nThis is the first article lemmatized: \n', articles_lemmatized)
    
    articles_as_BOW=[] #bag of words
    for a in articles_lemmatized:
        if a:
            a_words=[]
            for sentence in a:
                a_words=a_words+sentence
            articles_as_BOW.append(a_words)
    
    print('\nThis is the first article as BOW: \n', articles_as_BOW)
    #print('\nThere are %d articles in %s\n' %(len(articles_as_BOW), fname))
    
    fname=fname[:7]
    output=open(fname+'_articles_as_BOW.pkl', 'wb')
    dump(lemmas, output, -1)
    output.close()
    
    return articles_as_BOW """

'''test if run as application'''
if __name__=='__main__':
    texts_as_BOW=prepare_texts('C:\\Users\\navi_\\Desktop\\SFU_Spanish_Review_Corpus\\moviles\\')
    

    
