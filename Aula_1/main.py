#Aula 1 - Bootcamp Python

print("Primeiro código do bootcamp")

x = input("Digite seu nome: \n")


#Digite o seu nome e retorn o numeoro de carcaterers
print(f"Seu nome é {x}")
print(len(x))


#Crie um programa onde o usuario digita dois valores

y = int(input("Digite Primeiro Valor: \n"))
z = int(input("Digite Segundo Valor: \n"))

print(f'A soma dos valores é {y+z}')

#temos 4 tipos primitivos

numero = 3 #int
numero_decimal = 4.9 #float
verdadeiro = True #bool
falso = False #bool
texto = "Lucas" #string
#em python tudo é objeto
print(type(numero))
#python é case sensitive

_variavel_secreta = 10
#pra trazer mais seriedade a essa variavel

#o python tem uma tipagem dinamica , e isso é importante levar em consideração