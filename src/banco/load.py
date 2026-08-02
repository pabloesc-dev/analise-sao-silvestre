import pandas as pd
from sqlalchemy import create_engine
df = pd.read_csv('dados_tratados/sao_silvestre_historico_tratado.csv')

#conexão
engine = create_engine(
    "postgresql+psycopg2://postgres:SUA_SENHA@localhost:5433/sao_silvestre"
    )

df.to_sql(
            
    con=engine,
    if_exists = 'append',
    index = False
)