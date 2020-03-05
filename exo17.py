
def saisi_matrice (n,m) : 
    tab = []
    for i in range (n) :
        tab2 = []
        for j in range (m):
            print("Entrez un le composant : [", i , " ", j , "]")
            tab2.append(input(""))
        tab.append(tab2)
        #tab.append(int(input("Entrez un nombre: ")))
    return tab


def Produit_matrice(tab1,tab2,n,m,p):
    temp1=[]
    for i in range (n):
        temp2=[]
        for j in range (p):
            som=0
            for l in range (m):
                som+=(int(tab1[i][l]))*(int(tab2[l][j]))
            temp2.append(som)
        temp1.append(temp2)
    return temp1



def afficher_tableau (tab) : 
    for el in tab :
        line = ""
        for e in el :
            line = line + str(e) + " "
        print(line)



print ("Ce programme permet de calculer le produit de deux matrices de taille (N,M) et (M,P) ")
resultat=[]
N=int (input (" N = "))
M=int (input ("      M = "))
P=int (input ("             P = "))
print ("Saisi de la premiere matrice a ",N,"lignes et ",M, "Colonnes" )
tableau1=saisi_matrice(N,M)
print ("Saisi de la deuxieme matrice a ",M,"lignes et ",P, "Colonnes" )
tableau2=saisi_matrice(M,P)
print ("Le Produit du premier tableau")
afficher_tableau(tableau1)
print ("avec le second Tableau ")
afficher_tableau(tableau2)
resultat=Produit_matrice(tableau1,tableau2,N,M,P)
print ("est egale a    ")
afficher_tableau(resultat)


