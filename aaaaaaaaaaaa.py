from os import system
system("cls")

pagar=20000
descuento= pagar*0.25
monto_descuento=pagar-descuento
p1=input("usted pertenece a la florida ")
if p1=="no":
    print("vuelva pronto ")
if p1=="si":
    p2=input("usted tiene carnet de socio ")
    if p2=="no":
        carnet=input("cree su carnet aqui ")
    if p2=="si":
        input("ingrese su numero ")
        estado=input("usted es jubilado? ")
        if estado=="no":
            print(f"su monto a pagar es de {pagar}")
        if estado=="si":
            print(f"su monto a pagar es de {monto_descuento}")
        