import random
from os import system
system("cls")

jugador1=60
jugador2=60

def golpe():
    return random.randint(2,10)
def critico():
    return random.randint(1,5)
def miss():
    return random.randint(1,20)
def blockeo():
    return random.randint(1,10)

while True:
    j=input("quieres dar un golpe: ")
    if j=="si":   
        for i in range(2):
            if i+1==1:
                puño=golpe()
                criti=critico()
                fallo=miss()
                block=blockeo()
                jugador2=jugador2-puño
                print("bien le quitaste",puño,"de vida al jugador 2")
                print("jugador 1 te queda",jugador1,"de salud")
                if block==blockeo:
                    puño=puño+0.01
                    print ("el golpe fue bloqueado el daño fue reducido")
                if fallo==miss:
                    jugador2=jugador2-0
                    print ("fallaste el golpe")
                if criti==critico:
                    puño=puño*1.6
                    print ("bien le pegaste un critico al jugador 2")
            if i+1==2:
                puño=golpe()
                criti=critico()
                fallo=miss()
                jugador1=jugador1-puño
                print("bien le quitaste",puño,"de vida al jugador 1")
                print("jugador 2 te queda",jugador2,"de salud")
                input("enter para continuar")
                system("cls")
                if block==blockeo:
                    puño=puño+0.01
                    print ("el golpe fue bloqueado el daño fue reducido")
                if fallo==miss:
                    jugador1=jugador1-0
                    print ("fallaste el golpe")
                if criti==critico:
                    puño=puño*1.6
                    print ("bien le pegaste un critico al jugador 1")
    if j=="no":
        break
    if jugador1<=0:
        print("perdiste jugador 1, gana el jugador 2")
        break
    if jugador2<=0:
        print("perdiste jugador 2, gana el jugador 1")
        break
    