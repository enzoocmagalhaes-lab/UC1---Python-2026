produto = 1
soma = 0

while produto != 0:
    produto = float(input('Digite o numero do preço de seu pedido: '))
    soma = soma + produto
else:
    p = soma * 1.10
    print(f'o seu pedido de R$ {soma}, com mais 10%, dá um total de: {p:.2f}')