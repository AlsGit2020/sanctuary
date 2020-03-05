Tab=[]

print("Ce programme permet de construire le triangle de Pascal, a partir d'une taille de matrice donnee")
N=int (input (" Taille de la matrice N = "))

Tab = [[1],[1,1]]  # Les premiers elements du tableau de pascal

for i in range(2,N+1):
    Tab.append([1]) # initialisation de T[i][0] a 1
    for j in range(1, i):
        Tab[i].append(Tab[i-1][j-1] + Tab[i-1][j]) # les elements intermediaires obtenus par iteration
    Tab[i].append(1)  # initialisation pour T[i][i] a 1

for i in range (N+1): # Affichage du triangle de pascal
    print (Tab[i])






