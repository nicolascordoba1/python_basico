def es_primo(numero):
    if numero == 1:
        False
    else:
        contador = 0
        for i in range(1, numero+1):
            if i == 1 or i == numero:
                continue
            if numero % i == 0:
                contador +=1
        if contador == 0:
            True
        else: 
            False

def run():
    numero = int(input('Dame un número y te digo si es primo o no: '))

    if es_primo(numero):
        print('Es un número primo')
    else:
        print('No es un número primo')


if __name__ == '__main__':
    run()