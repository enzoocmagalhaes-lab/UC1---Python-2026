try:
    numerador = int(input('Digite o numero a ser divido: '))
    denominador = int(input('Digite o valor de divisão: '))

    resultado = numerador/denominador
    print(f'O resultado é {resultado}')

except ValueError:
    print('Digite apenas numeros inteiros.')

except ZeroDivisionError:
    print('Não pode dividir por zero.')