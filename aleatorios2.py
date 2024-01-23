'''
Script Description:
Cree una función que genere el lanzamiento de dos dados (1-6)
y que nos diga por pantalla el mensaje GANADOR cuando genere
un par, de lo contrario el mensaje dirá SIGUE INTENTANDO,
'''
#Import biblioteca para generar números aleatorios enteros
from random import randint
#Lanzar los dos dados
def dices():
    dice1=randint(1,6)
    dice2=randint(1,6)
    return dice1, dice2
#separar el arreglo
d = dices()
d0=d[0]
d1=d[1]
print("D1", d)
print("Dice1:",d0)
print("Dice1:",d1)

def lanzar(a,b):
    if a==b:
        print("GANADOR")
    else: 
        print("Sigue intentando")
    

lanzar(d0,d1)







