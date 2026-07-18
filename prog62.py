items = []
print('Lista de compras')
while True:
    colocar = input('Digite o seu produto (ou sair para parar): ')
    if colocar.lower() == 'sair':
        break

    items.append(colocar)
    print(f'Lista de compras: {items}')