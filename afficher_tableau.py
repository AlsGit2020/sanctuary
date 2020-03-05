# fonction permettant de saisir et d’afficher N éléments d’un tableau

def saisi_tableau (n) : 
    tab = []
    for i in range (n) :
        #tab[i] = int(input("Entrez un nombre: "))
        tab.append(int(input("Entrez un nombre: ")))

    return tab

def afficher_tableau (tab) : 
    for el in tab :
        print (el)

N=int (input ("Taille du tableau  N = "))
tableau = saisi_tableau(N)
afficher_tableau(tableau)