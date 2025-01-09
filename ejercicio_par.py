from os import system
system("cls")

e=int(input("ingrese un numero "))
for i in range(e+1):
    if i%2!=0:
        print("el numero es par", i)