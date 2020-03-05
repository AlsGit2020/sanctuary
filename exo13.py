print (" Ce programme permet de convertir un entier N écrit sous forme binaire en sa valeur décimale. ")

def bintodec(n):
    resultat = sum([2**i*int(n[::-1][i]) for i in range(len(n))])
    return resultat

N=input("Valeur en binaire N = ")
print ("L'equivalent en decimal est  = ", bintodec(N))

