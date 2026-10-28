def ciao(stringa_normale):
    lista = []
    stringa_normale = stringa_normale + "$"

    for i in range(len(stringa_normale)):
        lista.append(stringa_normale)
        
        stringa_normale = rearrangString(lista[i])


    sortStringAlphabetically(lista)
    print(lista)


        

def rearrangString(stringa):
    char_swp = stringa[0]
    stringa_new = stringa[1::]
    stringa_new = stringa_new + char_swp

    return stringa_new

def sortStringAlphabetically(lista):
    for i in range (len(lista)):
        for j in range(len(lista) - 1):
            if lista[j][0] > lista[j + 1][0]:
                parola = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = parola
        
    


ciao("banana")