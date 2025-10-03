import csv


path = "vendas.csv"

def ler_Csv(path) -> list:
    with open(path , mode= 'r' , encoding= 'utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        return list(leitor)

def processar_dados(lista):
    categorias = {}
    for item in lista:
        categoria = item['Categoria']
        if categoria not in categorias:
            categorias[categoria] = []
        categorias[categoria].append(item)
    return categorias


def calcular_vendas():
    pass

def exibir_resultados():
    pass


if __name__ == "__main__":
    x = ler_Csv(path)
    y = processar_dados(x)
    print(y)