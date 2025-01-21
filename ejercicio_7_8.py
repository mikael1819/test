from os import system
system("cls")

pin=8747
for i in range(3):
    pi=int(input("ingrese el pin por: "))
    if pi==pin:
        print ("si eres el dueño")
        break
    if pi!=pin:
        print("intento",i+1)
    if (i+1)==3:
        print("llamando a la policia")

# c1=int(input("ingrese el primer cateto: "))
# c2=int(input("ingrese el segundo cateto: "))
# if c1>0 and c2>0:
#     print("A²+B²=c²")
#     print(((c1**2)+(c2**2))**2)