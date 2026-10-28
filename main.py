def ciao(stringa_normale):
    lista = []
    stringa_normale = stringa_normale + "$"

    for i in range(len(stringa_normale)):
        lista.append(stringa_normale)
        
        stringa_normale = rearrangString(lista[i])
        

def rearrangString(stringa):
    char_swp = stringa[0]
    stringa_new = stringa[1::]
    stringa_new = stringa_new + char_swp

    print(stringa_new)
    return stringa_new

ciao("banana")