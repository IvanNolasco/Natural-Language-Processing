import nltk
from pickle import dump, load
from bs4   import BeautifulSoup
from nltk.corpus import cess_esp

def tag_sentences_nltk(sentences):
    for s in sentences:
        tokens=nltk.word_tokenize(s)
        s_tagged=nltk.pos_tag(tokens)
        print(s_tagged)


def tag_sentences_default_tagger(sentences, tag):
    default_tagger=nltk.DefaultTagger(tag)
    for s in sentences:
        tokens=nltk.word_tokenize(s)
        s_tagged=default_tagger.tag(tokens)
        print(s_tagged)

def tag_sentences_regexp_tagger(sentences):
    patterns=[ (r'.*o$', 'NMS'), # noun masculine singular
               (r'.*os$', 'NMP'), # noun masculine plural
               (r'.*a$', 'NFS'),  # noun feminine singular
               (r'.*as$', 'NFP')  # noun feminine singular
             ]
    
    regexp_tagger=nltk.RegexpTagger(patterns)
    for s in sentences:
        tokens=nltk.word_tokenize(s)
        s_tagged=regexp_tagger.tag(tokens)
        print(s_tagged)
       

def tag_spanish_sentences(sentences):
    #load the trained and saved Spanish tagger
    fname='UnigramTagger_cess_esp.pkl'
    input=open(fname, 'rb')
    tagger=load(input)
    input.close()
    tags_list = []
    for s in sentences:
        tokens=nltk.word_tokenize(s)
        s_tagged=tagger.tag(tokens)
        tags_list.append(s_tagged)
        #print(s_tagged)
    return tags_list
        
def tag_spanish_text(text):
    #load the trained and saved Spanish tagger
    fname='UnigramTagger_cess_esp.pkl'
    input=open(fname, 'rb')
    tagger=load(input)
    input.close()
    tokens=nltk.word_tokenize(text)
    s_tagged=tagger.tag(tokens)
    return s_tagged

def train_and_save_spanish_tagger():
    #train nltk.UnigramTagger using
    #tagged sentences from cess_esp 
    cess_tagged_sents=cess_esp.tagged_sents()
    tagger=nltk.UnigramTagger(cess_tagged_sents)
    
    #save the trained tagger in a file
    fname='UnigramTagger_cess_esp.pkl'
    output=open(fname, 'wb')
    dump(tagger, output, -1)
    output.close()
    
def get_sentences(fname):
    f=open(fname)
    t=f.read()
    soup = BeautifulSoup(t, 'lxml')
    text_string = soup.get_text()

    #get a list of sentences
    sent_tokenizer=nltk.data.load('nltk:tokenizers/punkt/english.pickle')
    sentences=sent_tokenizer.tokenize(text_string)
    return sentences

def get_nouns(lemmas_tags):
    """obtiene los sustantivos de una lista de lemmas"""
    nouns = []
    for lemma in lemmas_tags:
        """si la etiqueta es None porque no tiene lemma o es un sustantivo"""
        if lemma[1] == None or lemma[1][0] == 'n':
            """se agrega solamente el lemma"""
            nouns.append(lemma[0])
    return nouns

if __name__=='__main__':
    fname='C:\\Users\\navi_\\Dropbox\\NLP\\Corpus\\e960401.htm'
    sentences=get_sentences(fname)
    sentences=sentences[12:13]
    #tag_sentences_nltk(sentences)
    
    #example=['Sal de la ciudad rapidamente.']
    #tag_sentences_nltk(example)
    #print()
    #tag_spanish_sentences(example)
    
    #print()
    train_and_save_spanish_tagger()
    tag_spanish_sentences(sentences)
    
    #tag='sps00'
    #tag_sentences_default_tagger(sentences, tag)
    
    #tag_sentences_regexp_tagger(sentences)
  
    #nltk.help.upenn_tagset('VBZ')
    
    '''
    NNP proper noun singular
    NNS common noun plural
    VB  verb, base form
    VBZ verb, present tense, 3rd person singular
    VBD verb, past tense
    JJ adjective or numeral
    NN common noun, singular or mass
    IN preposition or conjunction
    FW foreign word
    PDT pre-determiner (e.g. all, both, many, such, this)
    DT determiner (e.g. another, each, no, some, all, both, this, these)
    '''
    