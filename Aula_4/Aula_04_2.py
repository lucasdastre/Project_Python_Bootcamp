import csv

caminho_arquivo = 'arquivo.csv'

arquivo_csv : list = []

'''DictReader lê cada linha do CSV como um dicionário (coluna: valor).

A primeira linha do CSV deve ser o cabeçalho com os nomes das colunas.

No final, arquivo_csv vai ser uma lista de dicionários, ex.:'''

#Gerenciador de contextos
# with open(caminho_arquivo , mode = 
#           'r' , encoding = 'utf-8') as arquivo:
#     leitor_csv =csv.DictReader(arquivo)

#     for linha in leitor_csv:
#         arquivo_csv.append(linha)

#     print(arquivo_csv)



    #funcoes

    #Empacotar uma funcao

lista_de_num = [1,2,3,4,1000,155, -500] 

def ordenar_lista(numero : list) -> list:
    nova_lista_numero = numero.copy()

    for i in range(len(nova_lista_numero)): 
        for j in range(i+1 , len(nova_lista_numero)):
            if nova_lista_numero[i] > nova_lista_numero[j]:
                nova_lista_numero[i] , nova_lista_numero[j] = nova_lista_numero[j] , nova_lista_numero[i]
    
    return nova_lista_numero

nova_lista = ordenar_lista(lista_de_num)
print(nova_lista)
