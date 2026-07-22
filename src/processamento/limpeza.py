import pandas as pd

df = pd.read_csv("dados_tratados/sao_silvestre_2025.csv")



def tempo_para_segundos(t):
    h, m, s = map(int, t.split(":"))
    return h * 3600 + m * 60 + s

def pace_para_segundos(p):
    m, s = map(int, p.split(":"))
    return m * 60 + s

df["tempo_segundos"] = df["tempo"].apply(tempo_para_segundos)
df["pace_segundos"] = df["pace"].apply(pace_para_segundos)

df.to_csv(
    "dados_tratados/sao_silvestre_2025_limpo.csv",
    index=False,
    encoding="utf-8-sig"
)
print(df.info())

print("\nValores nulos:")
print(df.isnull().sum())

print("\nDuplicados:")
print(df.duplicated().sum())