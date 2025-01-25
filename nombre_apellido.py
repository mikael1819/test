from os import system
system("cls")

nombres=[]

n=input("ingrese su nombre completo: ")
nombres.append(n)
for i in range(len(nombres)):
    print(len(nombres[i]))
p=n.split()
print(sorted(p))