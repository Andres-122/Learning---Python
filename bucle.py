'''Bucle loop, repetir una acción n veces
iteraciones 
contadores
acumuladores'''
#Función bucle para imprimir numeros del 1 al 10 en pantalla
def list_numbers():
    #Bucle imprime los numeros en pantallas
    i = 1
    while i <= 10:
        print(i)
        i = i + 1
        #i +=2 
    print("i: ",i)   

def list_number2():
    #Bucle imprime los numeros en pantallas
    i = 1
    status = True
    while status:
        if i == 11:
            break
        print(i)
        i = i + 1
    print("i: ",i)   
  
def list_number3():
    #Bucle imprime los numeros en pantallas
    i = 1
    status = True
    while status:
        print(i)
        i = i + 1
        if i > 10:
            status=False
    print("i: ",i)   

def list_number4():
    #Bucle imprime los numeros en pantallas
    i = 1
    status = False
    while not status:
        print(i)
        i = i + 1
        if i > 10:
            status=True
    print("i: ",i)   

#list_numbers()
#list_number2()
#list_number3()
list_number4()