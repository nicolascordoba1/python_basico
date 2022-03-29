def conversor(valor_dolar):
    moneda = float(input('Ingrese el valor a cambiar: '))
    conversion = round(moneda / valor_dolar, 2)
    conversion = str(conversion)
    print('Tienes '+ conversion + ' dolares')

usuario = int(input("""Que moneda vas a convertir a dólares. 
1)Pesos colombianos 
2)Pesos argentinos
3)Pesos mexicanos
"""))

if usuario == 1:
    conversor(3875)
elif usuario == 2:
    conversor(65)
elif usuario == 3:
    conversor(24)
else:
    print('Ingresa una opción correcta por favor')