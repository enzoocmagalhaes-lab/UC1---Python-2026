carros = {}
for i in range(2):
    carro = input('Digite o nome do carro: ')
    marca = input('Digite a marca do carro: ')
    valor = float(input('Digite o valor do carro: '))
    carros [carro] = {'marca': marca, 'valor': valor}
print(f'Lista de carros: {carros}')