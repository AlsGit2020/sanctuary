#initialisation tableau T a n elements
def saisi_tableau (n) : 
    tab = []
    for i in range (n) :
        tab2 = []
        for j in range (n):
            print("Entrez un le composant : [", i , " ", j , "]")
            tab2.append(input(""))
        tab.append(tab2)
        #tab.append(int(input("Entrez un nombre: ")))
    return tab


tabl = []
def fusion_tab(tab1,tab2):
    for element in tab1:
        tabl.append(element)
    for element in tab2:
        tabl.append(element)
    return tabl
    

N=int (input ("Taille du tableau  N = "))
M=int (input ("Taille du tableau  M = "))
tableau1=saisi_tableau(N)
print ("Tableau de taille N", tableau1)
tableau2=saisi_tableau(M)
print ("Tableau de taille M", tableau2)
resultat=fusion_tab(tableau1,tableau2)
print ("Fusion des tableau de taille N et M", resultat)



