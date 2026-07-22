import requests
import pandas as pd
from bs4 import BeautifulSoup
import time

url = "https://openresults.run/ajax_resultados_evento.cfm"

dados_finais = []

offset = 0
limit = 100

while True:

    params = {
        "id_evento": 28675,
        "modalidade": "15k",
        "genero": "M",
        "categoria": "",
        "equipe": "",
        "termo": "",
        "show_modalidade": 0,
        "show_categoria": 0,
        "offset": offset,
        "limit": limit,
        "busca": ""
    }

    try:

        resposta = requests.get(
            url,
            params=params,
            timeout=30
        )

        if resposta.status_code != 200:
            print(f"Erro HTTP: {resposta.status_code}")
            break

        dados = resposta.json()

    except requests.exceptions.RequestException as e:

        print(f"\nErro no offset {offset}")
        print(e)
        print("Tentando novamente em 10 segundos...\n")

        time.sleep(10)
        continue

    soup = BeautifulSoup(dados["html"], "html.parser")

    linhas = soup.find_all("tr")

    if len(linhas) == 0:
        print("\nFim dos resultados.")
        break

    for linha in linhas:

        colunas = linha.find_all("td")

        if len(colunas) >= 7:

            dados_finais.append({
                "colocacao": colunas[0].get_text(strip=True),
                "categoria": colunas[1].get_text(strip=True),
                "numero_peito": colunas[2].get_text(strip=True),
                "nome": colunas[3].get_text(strip=True),
                "equipe": colunas[4].get_text(strip=True),
                "pace": colunas[5].get_text(strip=True),
                "tempo": colunas[6].get_text(strip=True),
                "genero": "M"
            })

    print(f"Offset {offset} coletado | Registros: {len(dados_finais)}")

    if len(dados_finais) % 1000 == 0:

        pd.DataFrame(dados_finais).to_csv(
            "dados_brutos/backup_masculino.csv",
            index=False,
            encoding="utf-8-sig"
        )

        print("Backup salvo.")

    offset += limit

    time.sleep(0.5)

df = pd.DataFrame(dados_finais)

print("\nResumo:")
print(df["genero"].value_counts())
print("Total de registros:", len(df))
print("Dimensão:", df.shape)

df.to_csv(
    "dados_brutos/sao_silvestre_2025_masculino.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nArquivo salvo com sucesso.")