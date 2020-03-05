def factorielle (n):
    if n== 0 or n==1 :
        return 1
    else :
        return n*factorielle(n-1)

print ("Ce programme permet de calculer le factoriel d'un nombre ")
nombre = int (input ("Donner un nombre entier positif "))
while nombre <0 :
    nombre = int (input ("Donner un nombre entier positif "))
print ("le Factoriel de ", nombre , " =  ", factorielle(nombre))
