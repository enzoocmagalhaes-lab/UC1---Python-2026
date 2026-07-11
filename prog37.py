for i in range (4):
    aluno = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite as sua primeira nota: '))
    nota2 = float(input('Digite as sua segunda nota: '))
    nota3 = float(input('Digite as sua terceira nota: '))
    media = (nota1 + nota2 + nota3)/3
    if media >= 7:
        print(f'{aluno} tem uma media de {media:.1f} e está aprovado')
    elif media >= 5 and media <= 6:
        print(f'{aluno} tem uma media de {media:.1f} e está em recuperação')
    else:
        print(f'{aluno} tem uma media de {media:.1f} e está reprovado')