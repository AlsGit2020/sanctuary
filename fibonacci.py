def fibonacci (n):
    if n== 0 :
        return 0
    if n== 1 :
        return 1
    else :
        return fibonacci(n-1)+fibonacci(n-2)

print ("Ce programme permet de calculer la suite de Fibonacci d'un nombre")
nombre = int (input ("Donner un nombre entier positif  "))
while nombre <0 :
    nombre = int (input ("Donner un nombre entier positif  "))
print ("Fibonnacci de ", nombre , " =  ", fibonacci(nombre))