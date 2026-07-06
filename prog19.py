ingresso = input('Voce possui um ingresso (S ou N): ').upper()
if ingresso == 'N':
    print('Acesso Negado. Você precisa de um ingresso.')
elif ingresso == 'S':
    idade = int(input('Digite a sua idade: '))
    if idade < 12:
        print('Você tem o ingresso, mas não tem a idade mínima de 12 anos.')
    elif idade >= 12:
        print('Acesso liberado! Divirta-se no brinquedo.')