#O python tem inferencia automatica de variaveis
#tipagem dinamica

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