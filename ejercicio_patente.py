from os import system
system("cls")

patentes=[]
while True:
    print("1.ingrese una patente")
    print("2.borrar un patente")
    print("3.ver patentes")
    print("4.salir")
    opc=int(input("ingrese una patente: "))
    match opc:
        case 1:
            p=input("ingrese su patente: ")
            if p==patentes:
                print("la patente ya fue ingresada intentelo con otra")
            else:
                patentes.append(p)
            input("precione enter para continuar")
            system("cls")
        case 2:
            r=input("que patente quiere borrar: ")
            patentes.remove(r)
            input("precione enter para continuar")
            system("cls")
        case 3:
            print (patentes)
            input("precione enter para continuar")
            system("cls")
        case 4:
            print("vuelva pronto")
            break