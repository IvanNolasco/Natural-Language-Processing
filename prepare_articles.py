import nltk
import re
import operator
from pickle import dump, load
from split_articles import split_into_articles
from condentropy import getSentences
from test_tagging import get_nouns

def nouns_frq(nouns, tokens):
    nouns_frq_dict={}
    for n in nouns:
        nouns_frq_dict[n]=tokens.count(n)
    return nouns_frq_dict

def topics_article(articles, words):
    probs=[]
    i=1
    print('article \t',words[0], '\t',words[1], '\t',words[2], '\t',words[3], '\t',words[4], '\t',)
    for a in articles:
        art=[]
        sum = a.count(words[0])+a.count(words[1])+a.count(words[2])+a.count(words[3])+a.count(words[4])
        linea=str(i)+'\t'
        for w in words:
            if sum != 0:
                prob = a.count(w)/sum
            else:
                prob = 0
            linea = linea + str(prob) + "\t"
            art.append(prob)
        print(linea+'\n')
        probs.append(art)
        i+=1
    
def prepare_articles(fname):
    articles=split_into_articles(fname) #a list of strings, each string is an article   
    #print('\nThis is the first article: \n', articles[1])
    print(articles)
    """
    #download the POS tagger
    input=open('UnigramTagger_cess_esp.pkl', 'rb')
    tagger=load(input)
    input.close()
    
    #POS tag articles
    articles_tagged=[]
    for a in articles[1:]:
        #get a list of sentences
        sentences=getSentences(a)
        #print(sentences)
        
        #tag sentences, a tagged sentence is a list of tuples,
        #each tuple includes 2 elements
        sentences_tagged=[]
        for s in sentences:
            s_tagged=tagger.tag(nltk.word_tokenize(s))
            sentences_tagged.append(s_tagged)
        articles_tagged.append(sentences_tagged)
        
    #print('\nThis is the first article tagged: \n', articles_tagged)
    #print(articles_tagged[0][0])
    #print(articles_tagged[0][1]) #print one tagged sentences
    #print(articles_tagged[0][1][0]) #print one tagged word in a sentence
    
    with open('stopwords_es.txt', encoding='utf-8') as f:
        stopwords=f.readlines()
        stopwords=[w.strip() for w in stopwords]
    #print(stopwords[:10])
    
    #remove stopwords   
    articles_without_stopwords=[]
    for a in articles_tagged: 
        a_clean=[]
        for sentence in a:
            sentence_clean=[]
            for word_tagged in sentence:
                if word_tagged[0] not in stopwords:
                    sentence_clean.append(word_tagged)
            a_clean.append(sentence_clean)
        articles_without_stopwords.append(a_clean)
    #print('\nThis is the first article without stopwords: \n', articles_without_stopwords)
        
    #remove words containing symbols other than letters    
    articles_without_symbols=[]
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
    for a in articles_without_symbols:
        a_lemmatized=[]
        for sentence in a:
            sentence_lemmatized=[]
            for word_tagged in sentence:
                if word_tagged[1]==None or word_tagged[1][0]=='F':
                    sentence_lemmatized.append(word_tagged)
                else:
                    if word_tagged in lemmas.keys():
                        lemma=lemmas[word_tagged]
                        sentence_lemmatized.append((lemma,word_tagged[1]))
                    else:
                        sentence_lemmatized.append(word_tagged)
            a_lemmatized.append(sentence_lemmatized)
        articles_lemmatized.append(a_lemmatized)
    #print('\nThis is the first article lemmatized: \n', articles_lemmatized)
    
    #articles with tags
    articles_tags_as_BOW=[] #bag of words
    for a in articles_lemmatized:
        if a:
            a_words=[]
            for sentence in a:
                a_words=a_words+sentence
            articles_tags_as_BOW.append(a_words)
    
    #articles just tokens        
    articles_as_BOW=[]
    for a in articles_tags_as_BOW:
        a_words=[]
        for tag in a:
            a_words.append(tag[0])
        articles_as_BOW.append(a_words)
    
    #print(articles_as_BOW)
        
    text_as_BOW=[]
    for a in articles_as_BOW:
        text_as_BOW = text_as_BOW + a
    #print(text_as_BOW)
       
    #getting the nouns of the text
    nouns_articles=[]
    for a in articles_tags_as_BOW:
        a_nouns=get_nouns(a)
        nouns_articles=nouns_articles+a_nouns
    nouns_articles = sorted(set(nouns_articles))
    
    nouns_frq_dict = nouns_frq(nouns_articles, text_as_BOW)
    nouns_frq_list = sorted(nouns_frq_dict.items(), key=operator.itemgetter(1), reverse=True)
    #print(nouns_frq_list)
    
    words=['nación','gobierno','presidente','terrorismo','empresa']
    #topics_article(articles_as_BOW, words)
    
    #print('\nThis is the first article as BOW: \n', articles_as_BOW)
    #print('\nThere are %d articles in %s\n' %(len(articles_as_BOW), fname))
    
    #output=open(fname+'_articles_as_BOW.pkl', 'wb')
    #dump(lemmas, output, -1)
    #output.close()
    
    return articles_as_BOW
    """

'''test if run as application'''
if __name__=='__main__':
    prepare_articles('C:\\Users\\navi_\\Dropbox\\NLP\\Corpus\\e960401.htm')    
    