from os import system
system("cls")

contraseña=int(input("ingrese unacontraseña de seguridad "))
system("cls")

print("hola te doy la bienvenida a mi juego")
for i in range (5):
    c=int(input("ingresa la contraseña "))
    if c==contraseña:
        print("felicidades")
        break
    if c>contraseña:
        print("el numero es denaciado alto")
    if c<contraseña:
        print("el numero es muy bajo")
    else:
        print("error")