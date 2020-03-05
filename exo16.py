print ("algorithme récursif pour calculer x^n , x et n positifs non nuls")

def puissance (x,n):
    if n==1 :
        return x
    else :
        return x*puissance(x,n-1)


X = int(input(" Entrez une valeur > 0 de la base X  = " ))
Exp = int(input(" Entrez la valeur > 0 de l'exposant Exp  = " ))
while X<0 or Exp<0 :
    X=int(input(" Entrez une valeur > 0 de la base X  = " ))
    Exp=int(input(" Entrez la valeur > 0 de l'exposant Exp  = " ))

print ("La valeur de ", X, "a la puissance ", Exp , "est egale a ", puissance(X,Exp))
