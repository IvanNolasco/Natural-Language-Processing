import sys
import nltk

def prepareTexts(path):
    #se obtienen los nombres de los archivos en el directorio path
    from nombre_archivos import get_files_name
    listNames = get_files_name(path, '.txt')
    
    sampleTexts = [] #list of thexts, each text is a string
    y = [] # y is the list of tags
    
    #hacemos el etiquetado de las opiniones no=0 yes=1
    for name in listNames:
        if name[:2] == 'no':
            y.append(0)
        else:
            y.append(1)
        
    #leemos el contenido de los archivos
    for file in listNames:
        f=open('C:\\Users\\navi_\\Desktop\\SFU_Spanish_Review_Corpus\\musica\\'+file)
        text=f.read()
        f.close()
        #print(text)
        sampleTexts.append(text)
    
    return sampleTexts, y

if __name__=='__main__':
    path = 'C:\\Users\\navi_\\Desktop\\SFU_Spanish_Review_Corpus\\musica'
    sampleTexts, y = prepareTexts(path)
    #print(sampleTexts[])
    #print(y)
    