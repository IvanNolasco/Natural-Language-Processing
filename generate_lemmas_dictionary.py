from pickle import dump

def generate_lemmas_dictionary(fname):
    with open(fname, encoding='latin-1') as f:
        lines = f.readlines()
    #print('There are %d lines in %s.' %(len(lines), fname))
    
    lemmas={}
    for line in lines:
        if line == '\n':
            pass
        else:
            line=line.replace('#', '')
            words = [w.strip() for w in line.split()]
            t=(words[0], words[-2].lower())
            lemmas[t]=words[-1]
    
    print('There are %d entries in %s.' %(len(lemmas), 'lemmas dictionary'))
    
    #save the dictionary in a file
    output=open('lemmas.pkl', 'wb')
    dump(lemmas, output, -1)
    output.close()

'''test if run as application'''
if __name__=='__main__':
    generate_lemmas_dictionary('generate.txt')