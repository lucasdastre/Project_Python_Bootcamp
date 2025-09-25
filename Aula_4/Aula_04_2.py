import csv

caminho_arquivo = 'arquivo.csv'

arquivo_csv : list = []

'''DictReader lê cada linha do CSV como um dicionário (coluna: valor).

A primeira linha do CSV deve ser o cabeçalho com os nomes das colunas.

No final, arquivo_csv vai ser uma lista de dicionários, ex.:'''

#Gerenciador de contextos
with open(caminho_arquivo , mode = 
          'r' , encoding = 'utf-8') as arquivo:
    leitor_csv =csv.DictReader(arquivo)

    for linha in leitor_csv:
        arquivo_csv.append(linha)

    print(arquivo_csv)

    