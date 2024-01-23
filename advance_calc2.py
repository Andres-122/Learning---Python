def calculator(x,y,z):
    if z == '1':
        return x+y
    elif z =='2':
        return x-y
    elif z == '3':
        return x*y
    elif z =='4':
        if y==0:
            return 'No es posible dividir entre 0'
        else:
            return x/y
    elif z == '5':
        if y==0:
            return 'No es posible dividir entre 0'
        return 'la suma es',x+y, 'la resta es',x-y, 'la multiplicación es', x*y, 'la división es', x/y
    else:
        return 'vuelve a intentarlo'
    

n1 = float(input("Ingrese primer número"))
n2 = float(input("Ingrese segundo número"))
print(":::  MENÚ CALCULADORA :::")
print("[1]. Suma")
print("[2]. Resta")
print("[3]. multiplicación")
print("[4]. diviión")
print("[5]. Todas")
opc = input("Digite una opción del menú")

ans = calculator(n1,n2,opc)
print("resultado ", ans)