import csv
import pandas as pd

path = "Aula_7/vendas.csv"

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


def calcular_vendas_por_categoria(dados_por_categoria):
    resultado = {}
    for categoria, itens in dados_por_categoria.items():
        vendas_por_produto = {}
        for item in itens:
            produto = item.get('Categoria')
            try:
                valor = float(item.get('Venda', 0))
            except ValueError:
                valor = 0
            if produto in vendas_por_produto:
                vendas_por_produto[produto] += valor
            else:
                vendas_por_produto[produto] = valor
        resultado[categoria] = vendas_por_produto
    return resultado

def exibir_resultados(lista):
    #transformar em dataframe
    #funcao melt unpivota um daframe
    df = pd.DataFrame(lista)
    df_reset = df.reset_index().rename(columns={'index': 'Origem'})
    df_meltado = pd.melt(df_reset, id_vars=['Origem'], value_name='Valor')
    df_meltado = df_meltado.dropna(subset=['Valor'])
    df_meltado = df_meltado.drop(columns ='Origem')
    print(df_meltado)


if __name__ == "__main__":
    x = ler_Csv(path)
    y = processar_dados(x)
    z = calcular_vendas_por_categoria(y)
    w = exibir_resultados(z)