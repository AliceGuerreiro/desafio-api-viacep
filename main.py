import csv
import requests

ceps = [
    "01001000",
    "20040002",
    "30140071",
    "40010000",
    "50010000",
    "60060120",
    "70040900",
    "80010000",
    "90010000",
    "99999999"
]

resultados = []

for cep in ceps:
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()

        if "erro" in dados:
            resultados.append({
                "cep": cep,
                "logradouro": "",
                "bairro": "",
                "cidade": "",
                "uf": "",
                "ibge": "",
                "status": "CEP não encontrado"
            })
        else:
            resultados.append({
                "cep": dados.get("cep", cep),
                "logradouro": dados.get("logradouro", ""),
                "bairro": dados.get("bairro", ""),
                "cidade": dados.get("localidade", ""),
                "uf": dados.get("uf", ""),
                "ibge": dados.get("ibge", ""),
                "status": "OK"
            })

    except requests.RequestException:
        resultados.append({
            "cep": cep,
            "logradouro": "",
            "bairro": "",
            "cidade": "",
            "uf": "",
            "ibge": "",
            "status": "Erro ao consultar API"
        })

with open("enderecos.csv", "w", newline="", encoding="utf-8-sig") as arquivo:
    campos = ["cep", "logradouro", "bairro", "cidade", "uf", "ibge", "status"]

    escritor = csv.DictWriter(arquivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(resultados)

print("Arquivo enderecos.csv gerado com sucesso!")
