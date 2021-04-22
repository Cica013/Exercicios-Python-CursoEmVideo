from exe115.lib.interfaces import *
from exe115.lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arqExiste(arq):
    criarArquivo(arq)

cabeçalho('Sistema arquivo V1.0')
print()
cabeçalho('Menu interface')
while True:
    resp = menu(['Ver pessoas cadastradas.', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resp == 1:
        # listar conteúdo de um arquivo.
        lerArquivo(arq)
    elif resp == 2:
        # Opção cadastrar nova pessoa.
        cabeçalho('Novo cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabeçalho('Opção 3')
        cabeçalho('\033[1;4;36m Saindo do sistema... Até a próxima. \033[m')
        break
    else:
        print('\033[1;31mERRO... Digite uma opção válida.\033[m')
        print(linha())
