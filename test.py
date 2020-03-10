# ceci est un commentaire
binaire=input("Entrer le nombre binaire : ")
m=[]
for character in binaire:
    m.append(character)
    print(character)
print (m)

bintodec=0
j=0
for i in range (len(m)-1,-1,-1):
    bintodec += int (m[i])*pow(2,j)
    j+=1
print (bintodec)
# ceci est un autre commentaire 