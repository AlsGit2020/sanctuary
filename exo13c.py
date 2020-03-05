print (" Ce programme permet de convertir un entier N binaire en sa valeur décimale. ")

binaire=input("Entrer le nombre binaire a convertir : ")
m=[]
for character in binaire:
    m.append(character)

bintodec=0
j=0
for i in range (len(m)-1,-1,-1):
    bintodec += int (m[i])*pow(2,j)
    j+=1

print ("L'equivalent du binaire ", binaire, "  en decimal est  = ", bintodec)
