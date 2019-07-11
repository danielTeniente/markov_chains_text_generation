from scipy import stats
import numpy as np
import matplotlib.pyplot as pl
#grafo 1
#To be or not
#t -> o
#o -> ' ',r,t
#' '-> b,o,n
#b-> e
#e-> ' '
#n-> o
#r-> ' '
def similarity(target, ind):
    return(1 - string_difference(target, ind)/len(ind))

def string_difference(target, test):
    match_pattern = zip(target, test)  #give list of tuples (of letters at each index)
    difference = sum(1 for e in match_pattern if e[0] != e[1])  #count tuples with non matching elements
    difference = difference + abs(len(target) - len(test)) 
    return(difference)
def Obtener_MatrizP (texto):
    pasos=len(texto)
    texto=list(texto)
    letras=list(set(texto))
    indices = {}
    i=0
    for letra in letras:
        indices[letra]=[i] 
        i+=1
    matrizP=np.zeros((len(letras),len(letras)))
    textos=[]
    for char in letras:
        siguientes=[]
        for i in range(pasos-1):
            if(texto[i]==char):
                siguientes.append(texto[i+1])
        textos.append(list(set(siguientes)))
        divisor=len(textos[-1]) 
        for character in textos[-1]:
            matrizP[indices[char],indices[character]]=1/divisor
    return matrizP,indices

target=input("Ingrese el texto: ")
rep=int(input("Rep: "))
mostrar=int(input("Verbose: "))

tabla,indice=Obtener_MatrizP(target)
letras=list(set(target))


print("Generador de textos")

#simulacion

pasos=len(target)
target=list(target)

cont=0
respuesta=[]
inicio=indice[target[0]]

for j in range(rep):
    camino=[]
    camino.append(inicio)
    respuesta.append(target[0])
    for i in range(pasos-1):
        limites=np.array(tabla[camino[-1]])
        limites=np.cumsum(limites)
        if(limites.sum()!=0):
            camino.append(np.where(np.random.rand()<limites)[0][0])
            respuesta[j]+=letras[camino[-1]]
        
mejor=[0,'']
for text in respuesta:
    similaridad=similarity(target, text)
    if(similaridad>mejor[0]):
        mejor[1]=text
        mejor[0]=similaridad
    if(mostrar==1):
        print(text,' ',similaridad)
print('Mejor cadena:',mejor[1],' ',mejor[0])