from write import writeList

def lemmas_text(lemmas_dict, vocabulary):
    lemmas_text=[]
    for v in vocabulary:
        #se busca el lemma de la palabra en el diccionario
        lemma = lemmas_dict.get(v)
        #si se encontro el lemma y no está en la lista se agrega el lemma
        if lemma != None and lemmas_text.count(lemma)==0:
            lemmas_text.append(lemma)
            #sino se encontro se agrega la palabra 
        elif lemma == None and lemmas_text.count(lemma)==0:
            lemmas_text.append(v)
    return lemmas_text

def gen_lemmas(archivo):
	f=open(archivo)
	t=f.readline()
	d = {}
	while t != "":
		l = t.split()
		if l != []:
			l[0]=l[0].replace("#","")
			#g.write("%s %s\n" %(l[0],l[-1]))
			d.setdefault(l[0],l[-1])
		t=f.readline()
	f.close()
	return d

if __name__=='__main__':
    fname_vocabulary='C:\\Users\\navi_\\Dropbox\\NLP\\Programas\\e960401_vocabulary.txt'
    f_vocabulary=open(fname_vocabulary, encoding='utf-8')
    voc=f_vocabulary.read()
    vocabulary=voc.split()
    f_vocabulary.close()    
    fname_lemmas='C:\\Users\\navi_\\Dropbox\\NLP\\Programas\\generate.txt'
    lemmas_text_dict=gen_lemmas(fname_lemmas)
    lemmas_text_list=lemmas_text(lemmas_text_dict, vocabulary)
    writeList(lemmas_text_list, 'C:\\Users\\navi_\\Dropbox\\NLP\\Programas\\e960401_lemmas.txt')  