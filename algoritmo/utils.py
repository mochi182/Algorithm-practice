

def dameIndiceHijoIzquierdo(indicePadre):
    return int((2*indicePadre)+1)
def dameIndiceHijoDerecho(indicePadre):
    return int((2*indicePadre)+2)
def dameIndicePadre(indiceHijo):
    return int((indiceHijo-1)/2)

#---------------------#

def tieneHijoIzquierdo(indice):
    return dameIndiceHijoIzquierdo(indice) < len(lista)
def tieneHijoDerecho(indice):
    return dameIndiceHijoDerecho(indice) < len(lista)
def tienePadre(indice):
    return dameIndicePadre(indice) >= 0

#---------------------#

def hijoIzquierdo(indice):
    return lista[dameIndiceHijoIzquierdo(indice)]
def hijoDerecho(indice):
    return lista[dameIndiceHijoDerecho(indice)]
def padre(indice):
    return lista[dameIndicePadre(indice)]

#---------------------#

def intercambio(indiceUno, indiceDos):
    temp = lista[indiceUno]
    lista[indiceUno] = lista[indiceDos]
    lista[indiceDos] = temp

def extraerCima():
    listaOrdenada.insert(0,lista[0])
    lista[0] = lista[len(lista)-1]
    lista.pop()
    heapificar()
    return None

def heapificar():
    indice = 0
    while(tieneHijoIzquierdo(indice)):
        indiceGrande = dameIndiceHijoIzquierdo(indice)
        if (tieneHijoDerecho(indice) and hijoDerecho(indice) >  hijoIzquierdo(indice)):
            indiceGrande = dameIndiceHijoDerecho(indice)

        if lista[indice] > lista[indiceGrande]:
            break
        else:
            intercambio(indice, indiceGrande)
        indice = indiceGrande

def propiedadHeap():
    switch = True
    while switch:
        switch = False
        for a in range(len(lista)-1, -1, -1):
            if tienePadre(a) and lista[a] > padre(a):
                intercambio(a, dameIndicePadre(a))
                switch = True

def suma(numero1, numero2):
    return numero1 + numero2