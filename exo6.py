def saisi_tableau (n) : 
    tab = []
    for i in range (n) :
        #tab[i] = int(input("Entrez la liste des nombres : "))
        tab.append(int(input("Entrez la liste des nombres : ")))
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
 
    
def recherche_dichotomique( element, liste_triee ):
    a = 0
    b = len(liste_triee)-1
    m = (a+b)//2
    while a < b :
        if liste_triee[m] == element :
            return True
        elif liste_triee[m] > element :
            b = m-1
        else :
            a = m+1
        m = (a+b)//2
    #if a==len(liste_triee)-1:
     #   return False
    if b <= a :
        return False



N=int (input ("Nombre des elements a trier  N = "))
t=saisi_tableau(N)
tf = quicksort(t)
print ("Liste initial ", t)
print ("Liste final apres triage : ", tf)

X=int (input ("L'element a trouver dans la liste  X = "))
n= recherche_dichotomique(X,tf)
print (n)

