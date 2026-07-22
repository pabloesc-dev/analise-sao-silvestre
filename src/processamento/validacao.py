import pandas as pd

df = pd.read_csv("dados_brutos/sao_silvestre_2025_feminino.csv")

print(df.head())
print()
print(df.info())
print()
print("Total de registros:", len(df))
print("Total de registros:", len(df))
print(df.shape)