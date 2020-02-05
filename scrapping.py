import bs4
import requests
import re
import shutil
import urllib


def openFile ():
    line=0
    archivo = open("links.txt",'r')
    for linea in archivo.readlines():
        print (linea)
        line=line+1
        downloadImages(linea,line)
    archivo.close()

def downloadImages(image,line):
    try:
        urllib.request.urlretrieve(image, "laptop-{}.jpg".format(line))
    except:
        print("Imagen no {} se encuentra dañada".format(line))
    

if  __name__ == "__main__":
    openFile()