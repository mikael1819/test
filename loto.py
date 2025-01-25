import random
from os import system
system("cls")

loto=[]
for i in range(7):
    num=random.randint(1,38)
    loto.append(num)
    loto.sort()
print(loto)