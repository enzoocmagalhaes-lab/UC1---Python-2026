produto = ''
soma = 0

while produto != '0':
    produto = (input('Digite o numero de seu produto: '))
    if produto == '001':
        soma = soma + 4.00
        print(f'O seu produto escolhido é Arroz e seu preço no total é {soma}')
    elif produto == '002':
        soma = soma + 7.00
        print(f'O seu produto escolhido é Feijão e seu preço no total é {soma}')
    elif produto == '003':
        soma = soma + 5.00
        print(f'O seu produto escolhido é Macarrão e seu preço no total é {soma}')
else:
    print(f'Sua soma total é {soma}')