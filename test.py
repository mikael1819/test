from os import system
system("cls")

edad=int(input("ingrese su edad "))
if edad<=12:
    entradas=int(input("cuantas entradas quiere "))
    precio_pagar= entradas*500
    print(f"su precio a pagar es de {precio_pagar}")
if edad>=13 and edad<=18:
    entradas=int(input("cuantas entradas quiere "))
    precio_pagar= entradas*1000
    print(f"su precio a pagar es de {precio_pagar}")
if edad>=19 and edad<=64:
     entradas=int(input("cuantas entradas quiere "))
     precio_pagar= entradas*2000
     print(f"su precio a pagar es de {precio_pagar}")
if edad>=65:
     entradas=int(input("cuantas entradas quiere "))
     precio_pagar= entradas*700
     print(f"su precio a pagar es de {precio_pagar}")





























