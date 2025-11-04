
import pandas as pd
import os
import glob


pasta = "data"
arquivos_json = glob.glob(os.path.join(pasta , '*.json'))
df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
df = pd.concat(df_list , ignore_index= True)

print(df)
# #uma funcao de extract

# def extract():

#     pass


# #uma funcao que transforma

# def tranform():
#     oass

# #uma funcao que da load em csv e parquet

# def load():
#     pass
