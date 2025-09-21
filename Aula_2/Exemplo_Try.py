#É importante conhecer os veirificadores

#try
#except
#finally
#isinstance

#exemplo de numero

# try:
#     len(3)
# except TypeError:
#     print("Ocorreu um erro erro de tipagem")
# finally:
#     print("Mas o importante é participar")


#is instance serve pra verificar se a variavel é doi tipo qe ele quer
x = int(input("Insira um numero: "))

try:    
    if(isinstance(x , int)):
        print("A variavel inserida é um inteiro")
    else:
        print("A variavel não é valida")

except Exception as e:
    print(e)