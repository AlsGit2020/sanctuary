def factorielle (n):
    if n== 0 or n==1 :
        return 1
    else :
        return n*factorielle(n-1)
print ("Ce programme permet de calculer l'arrangement de deux nombres n et p suivant la formule arr(n,p)=fact(n)/fact(n-p)")

def arrangement (a,b):
    return factorielle (a)/factorielle(a-b)


n = int (input ("Donner une valeur entiere et positive de n  "))   
p= int (input ("Donner la valeur entiere et positive de p tel que p<n "))

while n < p or n<0 or p<0 :
    n = int (input ("Donner une valeur entiere et positive de n  "))   
    p= int (input ("Donner la valeur entiere et positive de p tel que p<n "))

print ("L'arrangement de ", n , "et ", p , "est egal a  ", arrangement(n,p))