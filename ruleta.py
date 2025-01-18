import random
from os import system
system("cls")

def ruleta():
    return random.randint(1,6)

while True:
    print("bienvenido a mi lindo jugo seguro pasa sin miedo")
    jugar=input("quieres jugar?: ")
    if jugar=="si":
        print("bien te animaste")
        bala=ruleta()
        for i in range(6):
            print("listo es tu turno novato",i+1)
            m=input("para disparar presiona la p: ")
            if m=="f":
                if i+1==bala:
                    print("eres muy malo en este juego")
                    print("moriste")
                    break
                else:
                    print("bien te salvaste te voy a regalar 1000 pesos")
    if jugar=="no":
        print("naaaaaaa por culo juegas igual")
        bala=ruleta()
        for i in range(6):
            print("listo es tu turno novato",i+1)
            m=input("para disparar presiona la p: ")
            if m=="f":
                if i+1==bala:
                    print("eres muy malo en este juego")
                    print("moriste")
                    break
                else:
                    print("bien te salvaste te voy a regalar 1000 pesos")