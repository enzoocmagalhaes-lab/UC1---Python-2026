idade = float(input('Digite a sua idade: '))
if idade < 18:
    print('O/A candidata não está apto a participar')
elif idade >= 18:
    genero = input('Digite o seu genero (M ou F): ').upper()
    if genero == 'F':
        print('A candidata não está apto a participar')
    else:
        print('O candidata está apto a participar')
