from exe115.lib.interfaces import *


def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Algo deu errado na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso!!!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='Desconecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um Erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um Erro ao cadastrar uma pessoa.')
        else:
            print(f'Novo registro de {nome} cadastrado com sucesso.')
            a.close()
