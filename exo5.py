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
 
    

N=int (input ("Nombre des elements a triers  N = "))
t=saisi_tableau(N)
tf = quicksort(t)
print ("list initial ", t)
print ("t final : ", tf)
