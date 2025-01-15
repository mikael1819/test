from os import system
system("cls")


deuda=100000
pago=0

while True:
    print("1.Pago de Tarjeta de Crédito")
    print("2.Compras")
    print("3.salir")
    try:
        opc=int(input("ingrese una opcion: "))
        match opc:
            case 1:
                pago=int(input("ingrese un monto a pagar: "))
                if pago>=0 and pago<=deuda:
                    deuda=deuda-pago
                    print("su deuda ahora es de ",deuda)
                    input("precione enter para continuar")
                    system("cls")
                elif pago<0:
                    print("se paso del monto")
                input("precione enter para continuar")
                system("cls")
            case 2:
                system("cls")
                while True:
                    print("1.queque cannabico $1200")
                    print("2.alfajor cannabico $1000")
                    print("3.lecho cannabica $1500")
                    print("4.pizza con (oregano) $2000")
                    print("5.meta $1000")
                    print("6.aceite cannabico $4000")
                    print("7.hamburguesas cannabicas $3000")
                    print("8.salir")
                    opc2=int(input("compre lo que usted quiera: "))
                    if opc2==1:
                        deuda=deuda+1200
                        print("su deuda ahora es de ",deuda)
                        input("precione enter para continuar")
                        system("cls")
                    if opc2==2:
                        deuda=deuda+1000
                        print("su deuda ahora es de ",deuda)
                        input("precione enter para continuar")
                        system("cls")
                    if opc2==3:
                        deuda=deuda+1500
                        print("su deuda ahora es de ",deuda)
                        input("precione enter para continuar")
                        system("cls")
                    if opc2==4:
                        deuda=deuda+2000
                        print("su deuda ahora es de ",deuda)
                        input("precione enter para continuar")
                        system("cls")
                    if opc2==5:
                        deuda=deuda+1000
                        print("su deuda ahora es de ",deuda)
                        input("precione enter para continuar")
                        system("cls")
                    if opc2==6:
                        deuda=deuda+4000
                        print("su deuda ahora es de ",deuda)
                        input("precione enter para continuar")
                        system("cls")
                    if opc2==7:
                        deuda=deuda+3000
                        print("su deuda ahora es de ",deuda)
                        input("precione enter para continuar")
                        system("cls")
                    if opc2==8:
                        system("cls")
                        break
                    else:
                        print("ingrese un numero valido")
                        input("precione enter para volver")
                        system("cls")
            case 3:
                print("vuelva pronto")
                break
            case _:
                print("ingrese una opcion valida")
                input("precione enter para volver")
                system("cls")
    except:
        print("ingrese un numero")