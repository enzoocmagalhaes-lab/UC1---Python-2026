numero1 = int(input('Digite o seu primeiro numero: '))
numero2 = int(input('Digite o seu segundo numero: '))
menu = int(input('Digite o numero da operação (1 a 4) que quer: '))

match menu:
    case 1:
        total = numero1 + numero2
    case 2:
        total = numero1 - numero2
    case 3:
        total = numero1 * numero2
    case 4:
        total = numero1 / numero2

print(total)
print('teste commit')
print('Teste de push de vrscode')