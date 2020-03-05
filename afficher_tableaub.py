
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

def afficher_tableau (tab) : 
    for el in tab :
        line = ""
        for e in el :
            line = line + e + " "
        print(line)
        

N=int (input ("Taille du tableau  N = "))
tableau = saisi_tableau(N)
afficher_tableau(tableau)