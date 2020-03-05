print (" Ce programme permet de convertir un nombre entier decimal (base10) , sous forme binaire. ")

quotient=2
reste=0
temp=[]
nombre=int(input("Donner le nombre base 10, decimal a convertir en binaire "))
while quotient>=2 :
    quotient=nombre//2
    reste=nombre%2
    temp.append(reste)
    nombre=quotient
print (temp)

result=[]
for i in range (len(temp)):
    result.append(str(temp[i]))
print (result)

final=result[0]
for i in range (1,len(result)):
    final+=result[i]
print ("La valeur equivalente en binaire de ", nombre, "est egale a  ", int(final))