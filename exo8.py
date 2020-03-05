print ("'utilisateur d'entrer N valeurs qui seront ensuite stockés dans un tableau. ")
print ("Afficher la plus grande valeur, la plus petite valeur, la somme, le produit et la moyenne des éléments du tableau")

def saisi_tableau (n) : 
    tab = []
    for i in range (n) :
        #tab[i] = int(input("Entrez un nombre: "))
        tab.append(int(input("Entrez un nombre: ")))
    return tab


def quicksort(t):
    if t == []:
        return []
    else:
        pivot = t[0]
        t1 = []
        t2 = []
        for x in t[1:]:
            if x<pivot: 
                t1.append(x)
            else: t2.append(x)
        return quicksort(t1)+[pivot]+quicksort(t2)
    
def somme_tableau (t) : 
    tab = []
    somme = 0
    for i in range (len(t)) :
        somme = somme+t[i]
    return somme

def produit_tableau (t) : 
    tab = []
    produit = 1
    for i in range (len(t)) :
        produit = produit*t[i]
    return produit

def moyenne_tableau (t) : 
    moyenne = somme_tableau(t)/len(t)
    return moyenne



N=int (input ("Taille du tableau  N = "))
tableau1=saisi_tableau(N)
print ("Tableau correspondant: ", tableau1)
tableau2 = quicksort(tableau1)
print ("La plus petite valeur est = ", tableau2[0])
print ("La plus grande valeur est = ", tableau2[N-1])
print ("La somme des valeurs est  = ", somme_tableau(tableau1))
print ("Le produit des valeurs est  = ", produit_tableau(tableau1))
print ("La moyenne des valeurs est  = ", moyenne_tableau(tableau1))