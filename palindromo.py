def run():
    palindromo = input('Escribe un palíndromo: ')

    palabra = palindromo.lower().replace(' ', '')
    if palabra == palabra[::-1]:
        print('Es un palíndromo')
    else:
        print('No es palíndromo')


if __name__ == '__main__':
    run()    