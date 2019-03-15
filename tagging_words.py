"""
@author: navi_
"""
from clean_tokens import *
from mutual_information import *
import nltk
from write import writeList
from nltk.corpus import cess_esp
from mutual_information import getSentences      
     
def tag_spanish_sentence(sentence, tagger):
    tokens=nltk.word_tokenize(sentence)
    s_tagged=tagger.tag(tokens)
    return s_tagged
    

if __name__ == '__main__':
    """obteniendo el texto para tokenizar por oraciones"""
    """
    fname='C:\\Users\\navi_\\Dropbox\\NLP\\Corpus\\e960401.htm'
    text_string=get_text_string(fname)
    sentences = getSentences(text_string)
    sent = sentences[12]
    #print(type(sent))
    text = nltk.word_tokenize(sent)
    cad = nltk.Text(text)
    print(nltk.pos_tag(cad))
    """
    tagget_sents = cess_esp.tagged_sents()
    #print(tagget_sents)
    tagger = nltk.UnigramTagger(tagget_sents)
    #tagger.load(input)
