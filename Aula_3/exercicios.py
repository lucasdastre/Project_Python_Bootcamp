
#qtd e venda
# qtde = int(input("Insira a quantidade : "))

# valor = int(input("Insira o valor : "))

# if (qtde > 0) and (valor > 0) :
#     print("Valor e qtd corretos")

# else :
#     print("Valores incorretos")

#Laço for
#range não printa ultimo numero
# for i in range(2,6):
#     print(i)

# alunos = ["lucas" , "Gabriel" , "Marcia"]
# list(alunos)
# for alu in alunos:
#     print(alu)


#contagem de palavras em textos

texto = "Hoje é nossa segunda aula do bootcamp , bootcamp de python"
palavras = texto.split(" ")

print(palavras)
#dicionario pra coletar 
contagem_de_palavras =  {}

for palavra in palavras:
    
    if palavra in contagem_de_palavras:
        contagem_de_palavras[palavra] += 1
    else:
        contagem_de_palavras[palavra] = 1


print(contagem_de_palavras)