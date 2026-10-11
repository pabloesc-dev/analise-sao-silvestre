import os
import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('dados_tratados/sao_silvestre_historico_tratado.csv')

engine = create_engine(os.environ["DATABASE_URL"])

df.to_sql(
    name='resultados',
    con=engine,
    if_exists='append',
    index=False
)