import sys
import nltk

def prepareData(fname):
    ''' Input: 
            text file, each lines is a sample, 
            the last token in the line is the class label.
        Output: 
            sampleTexts = list of strings, each string is a sample;
            y = list of class labels.
    '''
    
    f=open(fname)
    lines=f.readlines()
    f.close()

    #check whether each text is tagged as spam or ham
    noTags=[]
    for line in lines:
        line=line.strip()
        if line != '':
            words=nltk.word_tokenize(line.strip())
            if words[-1] == 'spam' or words[-1] =='ham':
                pass
            else:
                noTags.append(lines.index(line)+1)
    if noTags:
        print('The following lines have no tags:')
        print(noTags)
        sys.exit()
       
    sampleTexts=[] #list of texts, each text is a string
    y=[]           #list of tags (categories) of the texts
    for line in lines:
        line=line.strip()
        if line != '':
            words=nltk.word_tokenize(line.lower())
            if words[-1]=='spam':
                y.append(1)
            elif words[-1]=='ham':
                y.append(0)
            del words[-2:]     #delete the last two elements (',' and 'spam') in the list
            sampleTexts.append(' '.join(words))
    
    return sampleTexts, y

if __name__=='__main__':
    fname = 'C:\\Users\\navi_\\Dropbox\\NLP\\Corpus\\SMS_Spam_Corpus.txt'
    sampleTexts, y = prepareData(fname)
    print(sampleTexts[:2])
    print(y)
    