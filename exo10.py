print ("Ce programme permet de calculer le nombre de fois pour lesquelles ")
print ("tous les éléments apparaît dans un tableau.")

def saisi_tableau (n) : 
    tab = []
    for i in range (n) :
        #tab[i] = int(input("Entrez un nombre: "))
        tab.append(int(input("Entrez un nombre: ")))

    return tab

def afficher_tableau (tab) : 
    for el in tab :
        print (el)



def unique (tab):
    unique=[]
    dejatrouve=[]
    for el in tab:
        if el not in dejatrouve:
            unique.append(el)
            dejatrouve.append(el)
    return unique




tableau = []
N=int (input ("Taille du tableau  N = "))
tableau = saisi_tableau(N)
afficher_tableau(tableau)
temp=unique(tableau)
print("Le tableau est", tableau)
print("Le tableau des elements unique est  ", temp)
for el in temp:
    if el in tableau:
        print ("Le nombre ", el , ' apparait ', tableau.count(el), " fois dans le tableau" )


