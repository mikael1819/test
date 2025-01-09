from os import system
system("cls")

total=0
for i in range(3):
    n=int(input("ingrese una nota "))
    total=total+n
print(f"su promedio es de {total/(i+1)}")
    
    