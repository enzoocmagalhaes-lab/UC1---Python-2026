def idade(anoN):
    idadeAtual = 2026 - anoN
    if idadeAtual < 18:
        print(f'usuário tem {idadeAtual}, então é menor de idade.')
    elif idadeAtual >= 18 and idadeAtual < 65:
        print(f'Usuário tem {idadeAtual}, então é maior de idade.')
    else:
        print(f'Usuário tem {idadeAtual}, então é um idoso.')

Ano_Nascimento = int(input('Digite o ano de nascimento: '))
idade(Ano_Nascimento)