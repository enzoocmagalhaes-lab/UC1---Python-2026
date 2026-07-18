mercado = []
while True:
    item = input('Digite o seu item: ')
    if item.lower() == 'sair':
        break
    elif item in mercado:
        print('Item já cadastrado')
    else:
        mercado.append(item)

    for x in mercado:
        print(x)