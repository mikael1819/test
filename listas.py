from os import system
system("cls")

while True:
    lista=[12,35,62,64,23]
    l=int(input("agregue un elemento a la lista: "))
    lista.append(l)
    print(lista)
    lista.insert(1,4)
    print(lista)
    lista.remove(4)
    print(lista)
    lista.sort()
    print(lista)
    lista.reverse()
    print(lista)