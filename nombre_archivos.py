# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 12:23:27 2018

@author: navi_
"""

import os

"""devuelve una lista con los nombres de los archivos en un directorio (path)"""
def get_files_name(path, ext):
    #path Variable para la ruta al directorio
     
    #Lista vacia para incluir los ficheros
    lstFiles = []
     
    #Lista con todos los ficheros del directorio:
    lstDir = os.walk(path)   #os.walk()Lista directorios y ficheros
     
     
    #Crea una lista de los ficheros txt que existen en el directorio y los incluye a la lista.
     
    for root, dirs, files in lstDir:
        for fichero in files:
            (nombreFichero, extension) = os.path.splitext(fichero)
            if(extension == ext):
                lstFiles.append(nombreFichero+extension)
                #print (nombreFichero+extension)
                 
    #print(lstFiles)
    return lstFiles

def filter_files(listFiles, text):
    filterFiles = []
    for f in listFiles:
        if text in f:
            filterFiles.append(f)
    return filterFiles
    
if __name__=='__main__':
    path = 'C:\\Users\\navi_\\Desktop\\corpusCine\\corpusCriticasCine'
    listFiles = get_files_name(path, '.xml')
    print(listFiles)
    #print(filter_files(listFiles, 'review'))