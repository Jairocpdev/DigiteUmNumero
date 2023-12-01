while True:
    numero = float (input('Digite um número: '))

    if numero < 0:
        print ('Este número é negativo. Programa encerrado')
        break

    elif numero == 0:
        print ('Este número é neutro.')

    else:
        print ('Você digitou um número positivo.')

    continuar = input('Deseja digitar outro número? Digite "sim" para continuar: ')
    
    if continuar.lower() != 'sim':

        print ('Programa encerrado.')
        break
