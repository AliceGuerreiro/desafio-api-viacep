# Estágio em Tecnologia & Inteligência Artificial — Marcus Peterson Advocacia

## Desafio

Desenvolver um script utilizando uma API pública e gratuita, realizando consultas para uma lista de 10 entradas e gerando um arquivo CSV organizado.

O programa também deve tratar erros, como entradas inválidas ou indisponibilidade da API, sem interromper sua execução.

## API utilizada

Foi utilizada a API pública ViaCEP, que permite consultar informações de endereço a partir de CEPs brasileiros.

## Tecnologias utilizadas

- Python
- ViaCEP API
- Google Colab
- GitHub
- ChatGPT

## Funcionamento

O script:

1. Percorre uma lista com 10 CEPs.
2. Consulta cada CEP utilizando a API ViaCEP.
3. Coleta informações como:
   - CEP
   - Logradouro
   - Bairro
   - Cidade
   - UF
   - Código IBGE
4. Trata entradas inválidas, CEPs inexistentes e erros de comunicação com a API, sem interromper a execução.
5. Gera o arquivo `enderecos.csv` com os resultados.

## Arquivos do projeto

- `main.py` — código Python responsável pelas consultas e geração do CSV.
- `enderecos.csv` — arquivo gerado com os resultados das consultas.
- `prompts_ia.md` — histórico de uso de Inteligência Artificial durante o desenvolvimento.
- `README.md` — documentação do projeto.

## Como executar

Instale a biblioteca `requests`, caso ainda não esteja disponível:

```bash
pip install requests
