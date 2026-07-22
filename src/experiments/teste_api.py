import requests

URL = "https://openresults.run/ajax_resultados_evento.cfm"

params = {
    "id_evento": 28675,
    "modalidade": "15K",
    "genero": "M",
    "offset": 0,
    "limit": 5
}

print("Enviando requisição...")

try:
    resposta = requests.get(URL, params=params, timeout=15)

    print("Status:", resposta.status_code)
    print("URL:", resposta.url)
    print()
    print(resposta.text[:1000])

except Exception as e:
    print("Erro:", e)