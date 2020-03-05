print("Ce programme permet d'afficher les nombres de 0 a 1000, dont la somme des chiffres inferieur a 12")


def somme(nombre):
    som=0
    for element in nombre :
        chiffre = int(element)
        som += chiffre
    return som

LesNombre=""

for i in range (1001):
    if somme(str(i))<12:
        LesNombre+=str(i)+" "
print(LesNombre)
