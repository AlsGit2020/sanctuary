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

def Somme_matrice(tab1,tab2,n,m):
    temp=[]
    tabl=[]
    for i in range (n):
        for j in range (m) :
            temp.append((tab1[i][j]) + (tab2[i][j]))
        tabl.append(temp)
        temp=[]
    return tabl

def afficher_tableau (tab) : 
    for el in tab :
        line = ""
        for e in el :
            line = line + str(e) + " "
        print(line)

N=int (input ("Nombre de ligne  N = "))
M=int (input ("Nombre de colonne  M = "))
print ("Saisi de la premiere matrice a ",N,"lignes et ",M, "Colonnes" )
tableau1=saisi_matrice(N,M)
print ("Saisi de la deuxieme matrice a ",N,"lignes et ",M, "Colonnes" )
tableau2=saisi_matrice(N,M)
print ("La Somme du premier tableau")
afficher_tableau(tableau1)
print ("avec le second Tableau ")
afficher_tableau(tableau2)
resultat=Somme_matrice(tableau1,tableau2,N,M)
print ("est egale a    ")
afficher_tableau(resultat)


