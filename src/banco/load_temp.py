from sqlalchemy import create_engine

engine = create_engine(
    'postgresql://postgres:admin@localhost:5432/sao_silvestre'
)

with engine.connect() as conexao:
    print("Conectado com sucesso!")