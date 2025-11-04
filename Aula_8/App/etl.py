
import pandas as pd
import os
import glob

pasta = "data"
# #uma funcao de extract

def extract(pasta:str) -> pd.DataFrame: 
    arquivos_json = glob.glob(os.path.join(pasta , '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df = pd.concat(df_list , ignore_index= True)

    return df


# #uma funcao que transforma

def tranform(df:pd.DataFrame) -> pd.DataFrame:
    df['Total_vendas'] = df['Quantidade'] * df['Venda']

    return df

# #uma funcao que da load em csv e parquet

def load(df_final: pd.DataFrame) -> pd.DataFrame:
    df_final.to_csv("load/data_final.csv")
    df_final.to_parquet("load/data_final.parquet" , engine = 'pyarrow')
    # df_final.to_parquet()


def pipeline():
    df_extract = extract(pasta)
    df_etl = tranform(df_extract)
    load(df_etl)
    print('Pipeline rodou com sucesso')



if __name__ == '__main__':
    pipeline()