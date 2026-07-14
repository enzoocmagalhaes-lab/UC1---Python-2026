SENHA_CORRETA = 'python123'
tentativas = 0 
max_tentativas = 3

while tentativas < max_tentativas:
    tentativa = input(f'Digite a senha(Tentativa {tentativas + 1}/{max_tentativas}): ')
    if tentativa == SENHA_CORRETA:
        print('Acesso concedido! Bem-vindo.')
        break
    else:
        print('Senha Incorreta.')
        tentativas += 1
else:
    print('Você excede o número máximo em tentativas. Acesso bloqueado')