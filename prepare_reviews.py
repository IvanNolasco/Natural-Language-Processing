import nltk
import re
import operator
from pickle import dump, load
from split_articles import split_into_articles
from condentropy import getSentences
from test_tagging import get_nouns
from write import writeList
from prepareData_Cine import builtDict
from nombre_archivos import get_files_name
def nouns_frq(nouns, tokens):
    nouns_frq_dict={}
    for n in nouns:
        nouns_frq_dict[n]=tokens.count(n)
    return nouns_frq_dict
    
def prepare_articles(path):
    #obtenemos la lista de reviews en el path
    reviews=[]
    names = get_files_name(path, '.txt')
    #print(names)
    for n in names:
        f = open(path+n, encoding='latin-1')
        text = f.read()
        reviews.append(text)
    #download the POS tagger
    input=open('UnigramTagger_cess_esp.pkl', 'rb')
    tagger=load(input)
    input.close()
    
    #POS tag articles
    articles_tagged=[]
    sentences_tagged=[]
    for a in reviews:
        #get a list of sentences
        sentences=getSentences(a)
        
        #tag sentences, a tagged sentence is a list of tuples,
        #each tuple includes 2 elements
        #sentences_tagged=[]
        for s in sentences:
            s_tagged=tagger.tag(nltk.word_tokenize(s))
            sentences_tagged.append(s_tagged)
        articles_tagged.append(sentences_tagged)

    """         
    with open('stopwords_es.txt', encoding='utf-8') as f:
        stopwords=f.readlines()
        stopwords=[w.strip() for w in stopwords]
    
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
        
    text_as_BOW=[]
    for a in articles_as_BOW:
        text_as_BOW = text_as_BOW + a
       
    #getting the nouns of the text
    nouns_articles=[]
    for a in articles_tags_as_BOW:
        a_nouns=get_nouns(a)
        nouns_articles=nouns_articles+a_nouns
    nouns_articles = sorted(set(nouns_articles))
    
    nouns_frq_dict = nouns_frq(nouns_articles, text_as_BOW)
    nouns_frq_list = sorted(nouns_frq_dict.items(), key=operator.itemgetter(1), reverse=True)
    #print(nouns_frq_list[:50])
    #writeList(nouns_frq_list, 'sustantivos_moviles.txt')
    """
    return sentences_tagged

def compute_ngrams(sequence, n):
    return zip(*[sequence[index:] for index in range(n)])

def get_top_ngrams(corpus, ngram_val=1, limit=5):
    import operator
    tokens = nltk.word_tokenize(corpus)
    ngrams = compute_ngrams(tokens, ngram_val)
    ngrams_freq_dist = nltk.FreqDist(ngrams)
    sorted_ngrams_fd = sorted(ngrams_freq_dist.items(), key=operator.itemgetter(1), reverse=True)
    sorted_ngrams = sorted_ngrams_fd[0:limit]
    sorted_ngrams = [(' '.join(text), freq) for text, freq in sorted_ngrams]
    return sorted_ngrams

def get_polar_of_words(texts, words, dictS):
    sent_tok = nltk.data.load('nltk:tokenizers/punkt/english.pickle')
    pos = []
    neg = []
    cont = []
    for w in words:
        posaux = 0
        negaux = 0
        contaux = 0
        for t in texts:
            #sentences = sent_tok.tokenize(t.lower())
            sentences = nltk.sent_tokenize(t)
            for s in sentences:
                if w in s:
                    contaux += 1
                    tokens = nltk.word_tokenize(s)
                    for lemma in tokens:
                        if lemma in dictS:
                        #print(dict[lemma])
                            if dictS[lemma]=='pos':
                                posaux += 1
                            else:
                                negaux += 1
        if contaux > 0:
            pos.append(round(posaux/(posaux+negaux),4))
            neg.append(round(negaux/(posaux+negaux),4))
            cont.append(contaux)
        else:
            pos.append(0)
            neg.append(0)
            cont.append(0)
    return pos, neg, cont

def get_polar_words_of_text(texts, word, dictS):
    dictFrqPos = {}
    dictFrqNeg = {}
    for t in texts:
        #sentences = sent_tok.tokenize(t.lower())
        sentences = nltk.sent_tokenize(t)
        for s in sentences:
            if word in s:
                tokens = nltk.word_tokenize(s)
                for lemma in tokens:
                    if lemma in dictS:
                    #print(dict[lemma])
                        if dictS[lemma]=='pos':
                            if lemma in dictFrqPos:
                                dictFrqPos[lemma] += 1
                            else:
                                dictFrqPos[lemma] = 1
                        else:
                            if lemma in dictFrqNeg:
                                dictFrqNeg[lemma] += 1
                            else:
                                dictFrqNeg[lemma] = 1
                            
    dictPos = sorted(dictFrqPos.items(), key=operator.itemgetter(1), reverse=True)
    dictNeg = sorted(dictFrqNeg.items(), key=operator.itemgetter(1), reverse=True)
    return dictPos[:5], dictNeg[:5]

def get_sent_in_text_of_word(texts, word):
    sent = []
    for t in texts:
        #sentences = sent_tok.tokenize(t.lower())
        sentences = nltk.sent_tokenize(t)
        for s in sentences:
            if word in s:
                sent.append(s)
    return sent
                

'''test if run as application'''
if __name__=='__main__':
    sent_tag = prepare_articles('C:\\Users\\navi_\\Desktop\\SFU_Spanish_Review_Corpus\\moviles\\')
    print(sent_tag)
    
    """
    texts = []
    for r in reviews:
        texts.append(' '.join(r))
    #text = ' '.join(reviews)
    pos = []
    neg = []
    cont = []
    words = ['mano libres','pantalla','bateria','calidad','memoria', 'precio', 'juego', 'cámara']
    #pos, neg, cont = get_polar_of_words(texts, words,builtDict())
    """
    """
    for i in range(len(words)):
        print(words[i], '   pos =', pos[i], '   neg = ', neg[i], '   ocurrence = ', cont[i])
        i += 1
    """
    """
    #pos, neg = get_polar_words_of_text(texts, 'memoria' ,builtDict())
    sent = get_sent_in_text_of_word(texts, 'batería')
    print(sent)
    """
    #ngram = get_top_ngrams(text, 2, 10) 
    #print(ngram)
