def bwtAlgorithm(stringa_normale, trace):
    stringa_normale = stringa_normale.lower()
    lista = []
    lista_saved = []
    stringa_normale = stringa_normale + "$"

    for i in range(len(stringa_normale)):
        lista.append(stringa_normale)
        lista_saved.append(stringa_normale)
        stringa_normale = rearrangString(lista[i])


    lista = sortStringAlphabetically(lista)
    lista_saved = lista_saved + lista

    trasformata = getTrasformation(lista)
    lista_saved.append(trasformata)

    if(trace == True):
        return lista_saved
    else:
        return trasformata

def rearrangString(stringa):
    char_swp = stringa[0]
    stringa_new = stringa[1::]
    stringa_new = stringa_new + char_swp

    return stringa_new

def sortStringAlphabetically(lista):
    isSorted = False

    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            word1 = lista[j]
            word2 = lista[j + 1]
            if(isWordSorted(lista[j], lista[j + 1]) == False):
                parola = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = parola


    return lista

def isWordSorted(parola1, parola2):
    for i in range(len(parola1)):
        a = parola1[i]
        b = parola2[i]
        if parola1[i] > parola2[i]:
            return False
        elif parola1[i] < parola2[i]:
            return True
        
    return True
        
def getTrasformation(lista):
    stringa_trasformata = ""
    for i in range(len(lista)):
        stringa_trasformata = stringa_trasformata + lista[i][-1] 

    return stringa_trasformata




