import re
from bs4 import BeautifulSoup
from write import writeList
 
def split_into_articles(fname):
    """divide un texto en articulos, y a cada uno quita etiquetas html"""
    f=open(fname, 'r', encoding='latin-1') 
    t=f.read()
    f.close()
    text=t.replace(u'\x97', '') 
 
    #articles=re.split('<h3>', text) #articles is a list of strings
    articles=re.split(r'http://www.excelsior.com.mx/9604/960401/[\w]{3}[\d]{2}.html', text)
    arts=[]
    for article in articles:
        soup = BeautifulSoup(article, 'lxml') #article is a string
        text = soup.get_text()
        text=text.replace(u'\x97', '')
        arts.append(text)
     
    return arts #a list of strings, each string is an article
 
'''test if run as application'''
if __name__=='__main__':
    arts=split_into_articles('C:\\Users\\navi_\\Dropbox\\NLP\\Corpus\\e960401.htm')
    articles=arts[1:]
    #writeList(articles, 'articles.txt')
    #print('\n', 'This is the first article\n', articles[0], '\n')
    #print('This is the second article\n', articles[1], '\n')
    print('There are', len(articles), 'articles in e960401.html.')
    
    texto = 'C:\\Users\\navi_\\Dropbox\\NLP\\Corpus\\e960401.htm'
    
    """obtenemos una lista de articulos del texto, sin etiquetas html"""
    arts=split_into_articles(texto)
    articles=arts[1:]
    
    """de cada articulo dividimos en oraciones, y a su vez cada oracion dividimos en tokens"""
    tok_sent_art = [] #articulos dividido en oraciones divididas en tokens
    sent_art=[] #articulos dividio en oraciones
    for article in articles:
        sentences = getSentences(article.lower())
        aux_list = []
        art_aux = []
        for sent in sentences:
            tokens = get_clean_tokens(get_raw_tokens(sent))
            sent_aux = " ".join(tokens)
            art_aux.append(sent_aux)
            aux_list.append(tokens)
        sent_art.append(art_aux)
        tok_sent_art.append(aux_list)
    #print(tok_sent_art)
    #print(sent_art)
    
    sent_test = sent_art[0][12]
    print(sent_test)
    list_tags = tag_spanish_sentence(sent_test)
    for t in list_tags:
        print(type(t))
        print(t)