from os import system
system("cls")

par=[]
inpar=[]

p=int(input("ingrese un numero entero: "))
for i in range(p):
    if(i+1)%2==0:
        par.append(i+1)
    else:
        inpar.append(i+1)
print("los pares son",par)
print("los inpares son",inpar)