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
tabla=np.matrix([

                # t     o     r     b     n     e    ' '
                 [0,    1,    0,    0,    0,    0,    0], #t
                 [1/3,  0,  1/3,    0,    0,    0,    1/3], #o
                 [0,    0,    0,    0,    0,    0,    1], #r
                 [0,    0,    0,    0,    0,    1,    0], #b
                 [0,    1,    0,    0,    0,    0,    0], #n
                 [0,    0,    0,    0,    0,    0,    1], #e
                 [0,   1/3,   0,   1/3,   1/3,  0,    0],]) #' '

print("Generador de textos")

#simulacion
target='to be or not'
pasos=len(text)
letras=['t','o','r','b','n','e',' ']
rep=int(input())
mostrar=int(input())
cont=0
respuesta=[]
inicio=0
for j in range(rep):
    camino=[]
    camino.append(inicio)
    respuesta.append('t')
    for i in range(pasos-1):
        limites=np.array(tabla[camino[-1]])
        limites=np.cumsum(limites)
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