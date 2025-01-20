from os import system
system("cls")

p=""
t=0
iva=t*0.19/100
while True:
    print("los super volados")
    print("1. leche cannabica $2000")
    print("2. chocolate (normal) $4000")
    print("3. queque cannabica $4500")
    print("4. mistery box $1000")
    print("5. ir a pagar")
    print("6. salir")
    op=int(input("ingrese lo que quiere: "))
    match op:
        case 1:
            t=t+2000
            p=p+"leche cannabica\n"
            print("el precio del producto es de $2000")
            input("presione enter para continuar: ")
            system("cls")
        case 2:
            t=t+4000
            p=p+"chocolate (normal)\n"
            print("el precio del producto es de $4000")
            input("presione enter para continuar: ")
            system("cls")
        case 3:
            t=t+4500
            p=p+"queque cannabica\n"
            print("el precio del producto es de $4500")
            input("presione enter para continuar: ")
            system("cls")
        case 4:
            t=t+1000
            p=p+"mistery box\n"
            print("el precio del producto es de $1000")
            input("presione enter para continuar: ")
            system("cls")
        case 5:
            system("cls")
            while True:
                print("como quiere pagar")
                print("1. efectivo")
                print("2. debito")
                print("3. credito")
                op2=int(input("seleccione un meto de pago: "))
                match op2:
                    case 1:
                        tsin=t
                        iva=t+((t*19)/100)
                        print(f"los super volados\n{p}\n[subtotal (sin iva)={tsin} con un iva del = 19% total a pagar es de {iva}]")
                        break
                    case 2:
                        iva=t+((t*19)/100)
                        tsin=t
                        print(f"los super volados\n{p}\n[subtotal (sin iva)={tsin} con un iva del = 19% total a pagar es de {iva}]")
                        break
                    case 3:
                        t=t+((t*19)/100)
                        tsin=t
                        print(f"los super volados\n{p}\n[subtotal (sin iva)={tsin} con un iva del = 19% total a pagar es de {iva}]")
            break
        case 6:
            print("vuelva pronto")
            break