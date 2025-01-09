from os import system
system("cls")

t=0
n=input("ingre su nombre ")
for i in range (len(n)):
    t=t+(i+1)
    print("el total de la suma es",t)