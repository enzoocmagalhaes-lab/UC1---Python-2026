nome = input('Digite o seu nome: ')
nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
nota3 = float(input('Digite a sua terceira nota: '))
nota4 = float(input('Digite a sua quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4)/4
print(f'{nome}, sua média é {media:.1f}')
if media >= 6:
    print(f'{nome} está aprovado')
else:
    print(f'{nome} está em recuperação')