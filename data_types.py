#tipos de datos en pythons

#numericos
#pueden ser enteros z
num1=42
print(type(num1))
#numeros reales float
num2= 50.5
print(type(num2))
#Numeros complejos 
num3 = 2j
print(type(num3))

# datos tipo cadena
myname="Andres"
mylast_name='Rivera'
profile='''Es una persona sencilla
hola mundo'''
print(myname, type(myname))
print(mylast_name,type(mylast_name))
print(profile, type(profile))

#suma de cadenas concatenación
c="1"
d="130"
suma = c + d 
print(suma, type(suma)) 

#logico valores booleanos

usuario_activo = True
print("usuario_activo",type(usuario_activo))
pago_realizado = False
print("pago_realizado",type(pago_realizado))

#listas entre corchetes

frutas = ['apple', 'banana']
print(frutas)
print("frutas", type(frutas))
colors = ['green', 'blue','red']
print(colors)
print("colors", type(frutas))
detodito=['Andres',20,1520,'Chambu',1.70]
print(detodito)
print("detodito",type(detodito[1]))
