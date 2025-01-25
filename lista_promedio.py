from os import system
system("cls")


notas=[]
while True:
    n=int(input("ingrese la nota por favor: "))
    notas.append(n)
    if n==0:
        notas.remove(0)
        break
print(notas)
p=0
for i in notas:
    p+=i
    print(p/len(notas))