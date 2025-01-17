import random
from os import system
system("cls")

def dado():
    return random.randint(1,6)
    
ju1=1
ju2=2
paso1=0
paso2=0

print("bienvenidos al himalayas..... helados")
while True:
    print("holi bienvenido a mi ludo muy lindo y hermoso como el dueño ")
    print("jugador1")
    print("jugador2")
    print("salir")
    jugar=int(input("que jugador es: "))
    a=dado()
    if jugar==ju1:
        print("el jugador 1 avanza",a)
        paso1=paso1+a
        print("se le suman",paso1,"/ 24")
        input("enter para volver al menu ")
        system("cls")
        if paso1==24:
            print("usted gano")
            break
        elif paso1>24:
            print("usted se paso de pasos")
            paso1=paso1-a
            print("usted esta en la posicion",paso1)
    elif jugar==ju2:
        print("el jugador 1 avanza",a)
        paso2=paso2+a
        print("lleva",paso2,"/ 24")
        input("enter para volver al menu ")
        system("cls")