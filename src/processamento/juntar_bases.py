import pandas as pd


df_f = pd.read_csv(
    "dados_brutos/sao_silvestre_2025_feminino.csv"
)

df_m = pd.read_csv(
    "dados_brutos/sao_silvestre_2025_masculino.csv"
)

df_f["genero"] = "F"
df_m["genero"] = "M"


df = pd.concat(
    [df_f, df_m],
    ignore_index=True
)

print(df["genero"].value_counts())
print()
print("Total geral:", len(df))
print("Dimensão:", df.shape)

df.to_csv(
    "dados_tratados/sao_silvestre_2025.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nBase consolidada salva.")