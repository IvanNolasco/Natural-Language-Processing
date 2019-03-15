from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
import string
import gensim
from gensim import corpora
from prepare_articles import prepare_articles
 
#example documents
"""
doc1 = "Sugar is bad to consume. My sister likes to have sugar, but not my father."
doc2 = "My father spends a lot of time driving my sister around to dance practice."
doc3 = "Doctors suggest that driving may cause increased stress and blood pressure."
doc4 = '''Sometimes I feel pressure to perform well at school, 
       but my father never seems to drive my sister to do better.'''
doc5 = "Health experts say that sugar is not good for your lifestyle."
 
#compile documents
doc_complete = [doc1, doc2, doc3, doc4, doc5]
 
#clean documents
stop = set(stopwords.words('english'))
 
exclude = set(string.punctuation)
 
lemma = WordNetLemmatizer()
 
def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized
 
doc_clean = [clean(doc).split() for doc in doc_complete]
"""

articles_as_BOW=prepare_articles('C:\\Users\\navi_\\Dropbox\\NLP\\Corpus\\e960401.htm')
doc_clean = articles_as_BOW
#print(doc_clean)
 
'''Creating the term dictionary of our courpus, 
where every unique term is assigned an index.'''
dictionary = corpora.Dictionary(doc_clean) #a cada token le asigna un numero 
 
'''Converting list of documents (corpus) into 
Document Term Matrix using dictionary prepared above.'''
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean] #se mete la frecuencia de cada palabra
 
'''Creating the object for LDA model using gensim library'''
Lda = gensim.models.ldamodel.LdaModel
 
'''Running and Trainign LDA model on the document term matrix.'''
ldamodel = Lda(doc_term_matrix, num_topics=5, id2word = dictionary, passes=50)
 
print(ldamodel.print_topics(num_topics=5, num_words=8))


from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()
