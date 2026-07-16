def notas_de_alunos(n1, n2, n3, n4):
    media = (n1+n2+n3+n4)/4
    if media >= 7:
        print(f'Aluno tem uma média de {media:.1f}, está aprovado.')
    elif media <= 6 and media >= 5:
        print(f'aluno tem uma média de {media:.1f}, está em recuperação.')
    else:
        print(f'aluno tem uma média de {media:.1f}, está reprovado')

nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua nota: '))
nota3 = float(input('Digite sua nota: '))
nota4 = float(input('Digite sua nota: '))
notas_de_alunos(nota1,nota2,nota3,nota4)