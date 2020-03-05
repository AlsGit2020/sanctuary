print ("Cette fonction calcule la somme de nombres de 1 a n, si n > 0 et renvoie 0 sinon.")

def somme(n):
    if n>0 :
        return n + somme(n-1)
    else :
        return 0

N= int(input("Tapez le nombre N pour calculer la somme de 1 a N = "))

print ("la somme des nombres 0 a ", N, " est egale a :  ", somme(N))