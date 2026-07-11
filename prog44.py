nome = ''
while nome != 'SAI':
    nome = input('Digite o seu nome: ').upper()
    if nome == 'SAI':
        break
    print(f'Ola {nome}')