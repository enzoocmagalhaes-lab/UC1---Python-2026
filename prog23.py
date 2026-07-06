erro = int(input('Digite o seu codigo de erro: '))
match erro:
    case 200:
        print('Sucesso! Tudo certo com a sua requisição.')
    case 400:
        print('Erro de cliente: Requisição malformada.')
    case 401 | 403:
        print('Erro de permissão: Você não tem acesso a esta página.')
    case 404:
        print('Erro: Página não encontrada.')
    case 500 | 503:
        print('Erro no servidor: Nosso sistema está instável no momento')
    case _:
        print('Codigo HTTP desconhecido.')