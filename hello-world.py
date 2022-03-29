usuario = int(input("""Que moneda vas a cambiar. 
1)Dolares a pesos o 
2)Pesos a Dolares"""))

moneda = float(input('Ingrese el valor a cambiar: '))

precio_dolar = 3834.42

if usuario == 1:
    conversion = round(moneda * precio_dolar, 2)
    conversion = str(conversion)
    print('Tienes '+ conversion + ' pesos colombianos')
elif usuario ==2:
    conversion = round(moneda / precio_dolar, 2)
    conversion = str(conversion)
    print('Tienes '+ conversion + ' dolares')
else:
    print('Ingresa una opción correcta por favor')