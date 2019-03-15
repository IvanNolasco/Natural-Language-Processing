import nltk
from bs4   import BeautifulSoup
from write import writeList

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

def clean_tokens_from_initial_and_final_dash(raw_tokens):
    tokens_without_initial_and_final_dash=[] #tokens with starting or final dash deleted
    for tok in raw_tokens:
        if tok.startswith('-') or tok.endswith('-'):
            tok=tok.replace('-', '')
            if tok != '':
                tokens_without_initial_and_final_dash.append(tok)
        else:
            tokens_without_initial_and_final_dash.append(tok)
    print('There are', len(tokens_without_initial_and_final_dash), 'tokens without starting or final dash.\n')
    
    return tokens_without_initial_and_final_dash

def clean_tokens_from_internal_dash(tokens_without_initial_and_final_dash):
    tokens_with_internal_dash=[]
    for tok in tokens_without_initial_and_final_dash:
        if '-' in tok:
             tokens_with_internal_dash.append(tok)
    print('There are', len(tokens_with_internal_dash), 'tokens with internal dash.\n')
    print('These are tokens with internal dash:\n')
    print(tokens_with_internal_dash, '\n')
    
    strings_without_internal_dash=[]
    for tok in tokens_with_internal_dash:
        tok=tok.replace('-', ' ')
        strings_without_internal_dash.append(tok)
    print('There are', len(strings_without_internal_dash), 'strings with internal dash replaced by a space.\n')
    print('These are strings with internal dash replaced by a space:\n')
    print(strings_without_internal_dash, '\n')
        
    tokens_without_internal_dash=[]
    for string in strings_without_internal_dash:
        alist=nltk.Text(nltk.word_tokenize(string))
        alist=list(alist)
        tokens_without_internal_dash=tokens_without_internal_dash+alist
    
    print('There are', len(tokens_without_internal_dash), 'tokens without internal dash.\n')   
    print('These are tokens without internal dash:\n')
    print(tokens_without_internal_dash, '\n')
        
    #these are not all tokens from the file, only those which
    #had internal dash
    return tokens_without_internal_dash

if __name__=='__main__':
    fname='e960401.html'
    text_string=get_text_string(fname)
    raw_tokens=get_raw_tokens(text_string)
    tokens_without_initial_and_final_dash=clean_tokens_from_initial_and_final_dash(raw_tokens)
    #writeList(tokens_without_initial_and_final_dash, 'tokens_without_initial_and_final_dash.txt')

    #these are not all tokens from the file, only those which
    #had internal dash
    tokens_without_internal_dash=clean_tokens_from_internal_dash(tokens_without_initial_and_final_dash)