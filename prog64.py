carro = []
while True:
    items = input('Digite o seus carros: ')
    carro.append(items)
    quantidade = len(carro)
    if quantidade == 4:
        break

    for x in carro:
        print(x)

    