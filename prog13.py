nascimento = float(input('Digite o seu ano de nascimento: '))
idade = 2026 - nascimento
print(f'A idade do usuario é {idade:.0f} anos')
if idade > 18:
    print('Ele é maior de idade')
else:
    print('Ele é menor de idade')