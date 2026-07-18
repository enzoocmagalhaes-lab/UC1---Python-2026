cursos = ['Matematica', 'Engenharia']
item = input('Digite um curso: ')
cursos.append(item)
print('Listagem de cursos')
for i in cursos:
    print(i)
print('Escolha um curso para excluir')
curso = input('Digite um curso para excluir: ')
cursos.remove(curso)
for i in cursos:
    print(i)