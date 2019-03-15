import re
import imp
import mord as m
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
import numpy as np
from pprint import pprint

def build_and_evaluate_sklearn(sampleTexts, y):
    
    '''Build vector of token counts'''
    
    count_vect = CountVectorizer()
    X_counts = count_vect.fit_transform(sampleTexts) #list of texts, each text is a string
    X=X_counts
    print(X)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    #clf = LogisticRegression()
    clf = m.LogisticIT()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    print('Accuracy of prediction is', clf.score(X_test, y_test))
    print('Confusion matrix:\n', confusion_matrix(y_test, y_pred))
    print(metrics.classification_report(y_test, y_pred))



def prepareData(fname):
    f=open(fname, 'r', encoding='latin-1') 
    t=f.read()
    f.close()
    t=t.replace(u'\x97', '')
    X=re.split(',spam\n|,ham\n', t)
    Y = re.findall('spam|ham',t)
    for i in range(len(Y)):
        if Y[i] == 'ham':
            Y[i] = 0
        else:
            Y[i] = 1
    return X, Y 

if __name__=='__main__':
    sampleTexts, y = prepareData('C:\\Users\\navi_\\Dropbox\\NLP\\Corpus\\SMS_Spam_Corpus.txt')
    build_and_evaluate_sklearn(sampleTexts[:1000], y[:1000])





