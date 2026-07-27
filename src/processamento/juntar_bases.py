import pandas as pd

historico = pd.read_csv(
    "dados_brutos/sao_silvestre_historico.csv"
)

complemento = pd.read_csv(
    "dados_brutos/sao_silvestre_2022_2023.csv"
)

df_completo = pd.concat(
    [historico, complemento],
    ignore_index=True
)

print(df_completo.shape)

print(
    df_completo["ano"]
    .value_counts()
    .sort_index()
)

df_completo.to_csv(
    "dados_brutos/sao_silvestre_historico_completo.csv",
    index=False,
    encoding="utf-8-sig"
)