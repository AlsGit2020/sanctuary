def suite(n) :
    if n==0:
        return 2
    elif n==1:
        return 3
    else: 
        return (2/3)*suite(n-1)-(1/4)*suite(n-2)
       
print ("Ce programme permettant de calculer la valeur du N-ème")

N=int(input ("Donner la valeur de N entier positif <31 = "))
while N<0 :
    N=int(input ("Donner la valeur de N entier positif <31 = "))
while N>=31:
        N=int(input ("Donner la valeur de N entier positif <31= "))
print ("La valeur de la suite U( ", N ," ) = ", suite(N))
