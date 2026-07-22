import pandas as pd
from sqlalchemy import create_engine
df = pd.read_csv('../dados_tratados/sao_silvestre_2025_limpo.csv')
#conexão
engine = create_engine('postgresql://postgres:admin@localhost:5432/sao_silvestre')

df.to_sql(
    name = 'resultados',
    con=engine,
    if_exists = 'append',
    index = False
)