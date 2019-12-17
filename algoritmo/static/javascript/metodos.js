
// Obtiene índice de pariente

function dameIndiceHijoIzquierdo(indicePadre){
    return int((2*indicePadre)+1);}

function dameIndiceHijoDerecho(indicePadre){
    return int((2*indicePadre)+2);}

function dameIndicePadre(indiceHijo){
    return int((indiceHijo-1)/2);}

// Verifica pariente

function tieneHijoIzquierdo(indice){
    return dameIndiceHijoIzquierdo(indice) < len(lista);}

function tieneHijoDerecho(indice){
    return dameIndiceHijoDerecho(indice) < len(lista);}

function tienePadre(indice){
    return dameIndicePadre(indice) >= 0;}

// Obtiene pariente

function hijoIzquierdo(indice){
    return lista[dameIndiceHijoIzquierdo(indice)];}

function hijoDerecho(indice){
    return lista[dameIndiceHijoDerecho(indice)];}

function padre(indice){
    return lista[dameIndicePadre(indice)];}

// Funciones de ayuda

function intercambio(indiceUno, indiceDos){
    var temp = lista[indiceUno];
    lista[indiceUno] = lista[indiceDos];
    lista[indiceDos] = temp;
}

function extraerCima(){
    listaOrdenada.insert(0,lista[0]);
    lista[0] = lista[len(lista)-1];
    lista.pop();
    lista = heapificar(lista);
}

function heapificar()
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

function propiedadHeap(){
    var switch = True;
    while(switch){
            switch = False;
            for a in range(len(lista)-1, -1, -1):
                if(tienePadre(a) and lista[a] > padre(a)){
                    intercambio(a, dameIndicePadre(a));
                    switch = True;
                }
    }
    return lista;
}

function suma(numero1, numero2){
    return numero1 + numero2;
}