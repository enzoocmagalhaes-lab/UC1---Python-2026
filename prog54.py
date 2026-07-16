def por_cento(valor):
    return (valor*15)/100

v = int(input('Digite o seu valor: '))
por_centagem = por_cento(v)
print(f'Sua por centagem é {por_centagem}')