#O python tem inferencia automatica de variaveis
#tipagem dinamica

from typing import Dict
import json


idade : int = 30
nome : str= "Lucas"
dinheiro : float = 15.4
is_estudante : bool = True

#a partir do versão python 3.5 é possivcel fazer esse tipo de tipagem


#Exemplo lista

produto :str = "Sapato"
produto_2 :str = "chapeu"
produto_3 :str = "meia"

produtos : list = []

produtos.append(produto)
produtos.append(produto_2)
produtos.append(produto_3)

print(produtos)

produtos.pop(-2)
print(produtos)


#Exemplo Dicionario
# Chave : Valor

produto_1 = {
                "nome" : "Sapato",
                "Tamanho" : 39,
                "Cor": "Marrom",
                "Disponibilidade" : True
}


produto_2= {
                "nome" : "tenis",
                "Tamanho" : 42,
                "Cor": "azul",
                "Disponibilidade" : False
}

#Lista de items de dicionario

wish_list = []
wish_list.append(produto_1)
wish_list.append(produto_2)
print(wish_list)

#Transformando em json , um dicionario co particularidade da linguagem java script
wish_list_json = json.dumps(wish_list)
print(wish_list_json)

#Crie um dicionario que colete informações de um livro
#Titulo , autor , ano de publicação

Livros : list = []

ficar = True

while ficar:
    info = {
    "Livro" : str(input("Digite o nome do Livro :")),
    "Autor" : str(input("Digite o nome do Autor :")) , 
    "Ano" : str(input("Digite o nome do Ano :"))
    }

    resp = input("Voce deseja continuar no programa? : ")
    Livros.append(info)

    if resp == "Sim":
        ficar = False
        break
    else:
        continue
        
print(Livros)