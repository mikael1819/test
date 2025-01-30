from os import system
system("cls")

h=[
    [{},{},{},{},{},{}],
    [{},{},{},{},{},{}],
    [{},{},{},{},{},{}],
    [{},{},{},{},{},{}],
    [{},{},{},{},{},{}],
    [{},{},{},{},{},{}],
    [{},{},{},{},{},{}],
    [{},{},{},{},{},{}],
    [{},{},{},{},{},{}],
    [{},{},{},{},{},{}]
    ]
while True:
    print("1.agendar habitacion")
    print("2.ver estado hotel")
    print("3.vaciar habitacion")
    print("4.monetizar")
    print("5.salir")
    opc=int(input("que es lo que quiere hacer: "))
    match opc:
        case 1:
            p=int(input("en que piso quiere(1-10): "))-1
            a=int(input("en que habitacion quiere(1-6): "))-1
            n=input("ingrese su nombre por favor: ")
            if h[p][a]:
                print("esta habitacion esta ocupada")
                input("presione enter para volver a intentar")
                system("cls")
            else:
                h[p][a]=n
                input("presione enter para continuar")
                system("cls")
        case 2:
            print(h)
            input("presione enter para volver al menu")
            system("cls")
        case 3:
            p=int(input("en que piso esta la habitacion: "))-1
            a=int(input("cual es la habitacion: "))-1
            if h[p][a]:
                h[p][a]=[]
                print("la habitacion fue vaciada")
                input("presione enter para continuar")
                system("cls")
        case 4:
            hc=0
            total=0
            for i in h:
                if h [p][a]:
                    hc+=1
            tsiniva=hc*78500
            iva=tsiniva*0.19
            total+=iva
            print(" su total a pagar sin iva =",tsiniva,"\n sumando un iva del (19%) seria un total del",iva,"\n lo cual su total a pagar es de:",total)
            input("presione enter para volver al menu")
            system("cls")
        case 5:
            print("vuelva pronto")
            break
        case _:
            print("ingreso una opcion no valida")