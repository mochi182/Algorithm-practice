

def dameIndiceHijoIzquierdo(indicePadre):
    return int((2*indicePadre)+1)

def dameIndiceHijoDerecho(indicePadre):
    return int((2*indicePadre)+2)

def dameIndicePadre(indiceHijo):
    return int((indiceHijo-1)/2)

#---------------------#

def tieneHijoIzquierdo(indice, lista):
    return dameIndiceHijoIzquierdo(indice) < len(lista)

def tieneHijoDerecho(indice, lista):
    return dameIndiceHijoDerecho(indice) < len(lista)

def tienePadre(indice):
    return dameIndicePadre(indice) >= 0

#---------------------#

def hijoIzquierdo(indice, lista):
    return lista[dameIndiceHijoIzquierdo(indice)]

def hijoDerecho(indice, lista):
    return lista[dameIndiceHijoDerecho(indice)]

def padre(indice, lista):
    return lista[dameIndicePadre(indice)]

#---------------------#

def intercambio(indiceUno, indiceDos, lista):
    temp = lista[indiceUno]
    lista[indiceUno] = lista[indiceDos]
    lista[indiceDos] = temp
    return lista

#def extraerCima(lista):
#    listaOrdenada.insert(0,lista[0])
#    lista[0] = lista[len(lista)-1]
#    lista.pop()
#    lista = heapificar(lista)
#    return listaOrdenada

def extraerCima(lista):
    listaOrdenada = []
    lista = lista
    while len(lista)>0:
        listaOrdenada.insert(0,lista[0])
        lista[0] = lista[len(lista)-1]
        lista.pop()
        lista = heapificar(lista)
    return listaOrdenada

def heapificar(lista):
    indice = 0
    lista = lista
    while(tieneHijoIzquierdo(indice, lista)):
        indiceGrande = dameIndiceHijoIzquierdo(indice)
        if (tieneHijoDerecho(indice, lista) and hijoDerecho(indice, lista) >  hijoIzquierdo(indice, lista)):
            indiceGrande = dameIndiceHijoDerecho(indice)

        if lista[indice] > lista[indiceGrande]:
            break
        else:
            lista = intercambio(indice, indiceGrande, lista)
        indice = indiceGrande
    return lista

def propiedadHeap(lista):
    switch = True
    while switch:
        switch = False
        for a in range(len(lista)-1, -1, -1):
            if tienePadre(a) and lista[a] > padre(a, lista):
                lista = intercambio(a, dameIndicePadre(a), lista)
                switch = True
    return lista

def suma(numero1, numero2):
    return numero1 + numero2