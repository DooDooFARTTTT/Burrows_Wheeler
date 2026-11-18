#script effettivo richiamato poi dal server
def bwtAlgorithm(stringa_normale, trace):
    stringa_normale = stringa_normale.lower()       #tutta la stringa viene trasformata in caratteri lower
    lista = []                                      #viene salvato il contenuto delle varie combinazioni ottenute
    lista_saved = []                                #come lista, ma viene utilizzata se trace==True
    stringa_normale = stringa_normale + "$"         #aggiunta del dollaro alla fine della parola da trasformare
    
    #Prima fase, la stringa viene ruotata e le varie rotazioni salvate
    lista_saved.append("###PRIMA FASE###")      
    for i in range(len(stringa_normale)):                  
        lista.append(stringa_normale)
        lista_saved.append(stringa_normale + "\n")
        stringa_normale = rearrangString(lista[i])

    #Seconda fase, le rotazioni vengono poi ordinate alfabeticamente (lessico grafico) con il $ come valore minore
    lista = sortStringAlphabetically(lista)                 
    lista_saved.append("###SECONDA FASE###" + "\n")
    lista_saved = lista_saved + lista

    #Terza fase, si ottiene la trasformata data l'ultimo carattere delle rotazioni ordinate
    trasformata = getTrasformation(lista)                  

    lista_saved.append("\n" + "###RISULTATO###" + "\n")     
    lista_saved.append(trasformata)                         

    #se trace==True allora ritorna la lista con salvati tutti gli step dell'algoritmo, altrimenti ritorna solo la trasformata
    if(trace == True):                            
        return lista_saved
    else:
        return trasformata

#rotazione per singoila parola
def rearrangString(stringa):                
    char_swp = stringa[0]
    stringa_new = stringa[1::]
    stringa_new = stringa_new + char_swp

    return stringa_new


#effettua un sorting tra 2 rotazioni 
def sortStringAlphabetically(lista):
    isSorted = False

    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            word1 = lista[j]
            word2 = lista[j + 1]
            if(isWordSorted(lista[j], lista[j + 1]) == False):  #lo switch tra 2 rotazioni
                parola = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = parola


    return lista

#verifica lettera per lettera fino a quando una delle due lettere confrontate non è numericamente più grande
#se parola 1 è più piccola di parola 2, ritorna TRUE, altrimenti FALSE
def isWordSorted(parola1, parola2): 
    for i in range(len(parola1)):
        a = parola1[i]
        b = parola2[i]
        if parola1[i] > parola2[i]:
            return False
        elif parola1[i] < parola2[i]:
            return True
        
    return True

#prende l'ultima lettera da tutte le rotazioni sortate
def getTrasformation(lista):
    stringa_trasformata = ""
    for i in range(len(lista)):
        stringa_trasformata = stringa_trasformata + lista[i][-1] 

    return stringa_trasformata




