from Etl import ler_Csv , processar_dados , calcular_vendas_por_categoria , exibir_resultados

path_file = "Aula_7/vendas.csv"

x = ler_Csv(path_file)
y = processar_dados(x)
z = calcular_vendas_por_categoria(y)
w = exibir_resultados(z)