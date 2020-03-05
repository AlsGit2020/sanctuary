def saisi_matrice (n,m) : 
    tab = []
    for i in range (n) :
        tab2 = []
        for j in range (m):
            print("Entrez un le composant : [", i , " ", j , "]")
            tab2.append(int(input("")))
        tab.append(tab2)
        #tab.append(int(input("Entrez un nombre: ")))
    return tab

def Somme_diagonale(tab1,n):
    somme=0
    for i in range (n):
        for j in range (n) :
            if i== j :
                somme=somme+(tab1[i][j])
    return somme

def afficher_tableau (tab) : 
    for el in tab :
        line = ""
        for e in el :
            line = line + str(e) + " "
        print(line)



print ("Ce programme calcule la somme des éléments de la diagonale d’une matrice carrée M(n,n) donnée.")

N=int (input ("Saisir la dimeension de la matrice caree N = "))
print ("Saisi de la premiere matrice caree" )
tableau1=saisi_matrice(N,N)
print ("Voici la matrice carree : ")
afficher_tableau(tableau1)
resultat= Somme_diagonale(tableau1,N)
print ("La Somme des elements de la diagonale est: ", resultat)

