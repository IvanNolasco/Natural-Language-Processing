import sys
import nltk

def prepareTexts(path):
    #se obtienen los nombres de los archivos en el directorio path
    from nombre_archivos import get_files_name
    from nombre_archivos import filter_files
    #se recuperan los archivos con la extension .pos
    listNames = get_files_name(path, '.pos')
    #se filtran aquellos archivos .review para obtener X
    listFilesX = filter_files(listNames, 'review')
    #se recuperan los archivos .xml para obtener Y
    listFilesY = get_files_name(path, '.xml')
    
    #listFilesX = listFilesX[]
    #listFilesY = listFilesY[]
    
    sampleTexts = [] #list of thexts, each text is a string
    y = [] # y is the list of tags
    
    #recuperamos de cada texto X
    for f in listFilesX:
        sampleTexts.append(getX(path, f))
    
    for f in listFilesY:
        y.append(getY(path, f))
    
    return sampleTexts, y

def getX(path, fileName):
    f=open(path+'\\'+fileName)
    lines = f.readlines()
    f.close()
    lemmas = []
    for l in lines:
        tokens=nltk.word_tokenize(l)
        #print(tokens)
        #en caso de que este vacia la linea
        tokens.append(" ")
        tokens.append(" ")
        lemmaux = clean_lemma(tokens[1])
        lemmas.append(lemmaux)
    #IMPORTANTE PARA ENVIAR DATOS A MATRIZ, USAR:
    #return " ".join(lemmas)
    return lemmas

def clean_lemma(lemma):
    lemma = lemma.lower()
    lemma = lemma.replace('á','a')
    lemma = lemma.replace('é','e')
    lemma = lemma.replace('í','i')
    lemma = lemma.replace('ó','o')
    lemma = lemma.replace('ú','u')
    lemma = lemma.replace('ü','u')
    lemma = lemma.replace('ñ','n')
    return lemma

def getY(path, fileName):
    f=open((path+'\\'+fileName))
    text = f.read()
    f.close()
    text = text.replace('"',' ')
    list2 = text.split('rank=')
    tokens = nltk.word_tokenize(list2[1])
    #print(tokens[0])
    return int(tokens[0])

def getSenticonEs(path):
    dict = {}
    f=open(path, encoding='UTF-8')
    lines = f.readlines()
    f.close()
    lines = lines[4:-3] #-3
    #print(lines[0])
    for l in lines:
        tokens = nltk.word_tokenize(l)
        if len(tokens) > 8:
            pol = tokens[8]
            lemma = tokens[15]
            #print(lemma)
            dict[lemma] = pol
    return dict

def builtDict():
    dict = {}
    f = open('C:\\Users\\navi_\\Dropbox\\SpanishSentimentLexicons\\fullStrengthLexicon.txt')
    lines = f.readlines()
    f.close()
    f = open('C:\\Users\\navi_\\Dropbox\\SpanishSentimentLexicons\\mediumStrengthLexicon.txt')
    #lines = lines + f.readlines()
    f.close()
    for l in lines:
        tokens = nltk.word_tokenize(l)
        dict[tokens[0]] = tokens[-1]
    #print(dict)
    #print(len(dict))
    return dict

"""hace un promedio de la polaridad de las reseñas clasificando por categoria"""    
def classificationPol(texts, rank, dictSen):
    sums = [0, 0, 0, 0, 0]
    conts = [0, 0, 0, 0, 0]
    for i in range(len(texts)):
        #auxiliares para obtener el promedio de polaridad en cada reseña
        sumaux = 0
        contaux = 0
        for lemma in texts[i]:
            #print(lemma)
            if lemma in dictSen:
                sumaux += float(dictSen[lemma])
                contaux += 1
        #se guarda en el arreglo para clasificarlo po categoria
        #rank[i] nos da el ranking de la resseña y luego le restamos 1 para posicionarlo en el arreglo
        sums[rank[i]-1] += (sumaux)
        conts[rank[i]-1] += 1
        i += 1
        
    for j in range(len(sums)):
        print((j+1),' = ', (sums[j]/conts[j]))

"""hace un promedio de lemmas negativos y positivos en cada categoria de reseñas"""    
def classificationPol2(texts, rank, dict):
    pos = [0, 0, 0, 0, 0]
    neg = [0, 0, 0, 0, 0]
    conts = [0, 0, 0, 0, 0]
    for i in range(len(texts)):
        #auxiliares para contar positivos y negativos en cada resea
        posaux = 0
        negaux = 0
        for lemma in texts[i]:
            #print(lemma)
            if lemma in dict:
                #print(dict[lemma])
                if dict[lemma]=='pos':
                    posaux += 1
                else:
                    negaux += 1
        pos[rank[i]-1] += posaux
        neg[rank[i]-1] += negaux
        conts[rank[i]-1] += 1
        i += 1
        
    for j in range(5):
        print((j+1),'pos=', (pos[j]/conts[j]),' | neg=', (neg[j]/conts[j]))
        

if __name__=='__main__':
    path = 'C:\\Users\\navi_\\Desktop\\corpusCine\\corpusCriticasCine'
    #obtenemos lemmas y ranking de cada review
    sampleTexts, y = prepareTexts(path)
    pathDict = 'C:\\Users\\navi_\\Desktop\\ML-SentiCon\\senticon.es.xml'
    classificationPol2(sampleTexts, y, builtDict())
        