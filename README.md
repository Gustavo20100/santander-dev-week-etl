# Santander Dev Week 2023 — ETL com Python e OpenAI

Este projeto foi desenvolvido como parte do desafio **Santander Dev Week 2023**, com foco na construção de um pipeline **ETL (Extract, Transform, Load)** utilizando **Python** e **IA Generativa (OpenAI)**.

O objetivo é demonstrar o fluxo completo de dados, desde a extração até a persistência final, mesmo diante da indisponibilidade da API original do evento.

---

## 🚀 Objetivo do Projeto

Simular um cenário real onde um cientista de dados precisa:
- Extrair dados de clientes
- Transformar esses dados com mensagens personalizadas usando IA
- Persistir os resultados de forma estruturada

Tudo isso seguindo boas práticas de organização e versionamento de código.

---

## 🧩 Arquitetura ETL

### 🔹 Extract
- Leitura de dados a partir de um arquivo CSV (`SDW2023.csv`)
- Conversão para estrutura de dicionários em Python

### 🔹 Transform
- Geração de mensagens personalizadas sobre investimentos
- Utilização da API da OpenAI (GPT) para criação de conteúdo
- Cada cliente recebe uma mensagem individualizada

### 🔹 Load
- Persistência dos dados transformados em um arquivo `output.json`
- Substituição da etapa de PUT da API (indisponível)

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Pandas
- OpenAI API
- Git e GitHub

---

## 📂 Estrutura do Projeto

santander-dev-week-etl/
│
├── extract.py
├── transform.py
├── load.py
├── main.py
├── SDW2023.csv
├── requirements.txt
├── .gitignore
└── README.md


---

## ▶️ Como Executar o Projeto

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/SEU_USUARIO/santander-dev-week-etl.git
cd santander-dev-week-etl

2️⃣ Crie um ambiente virtual (opcional)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3️⃣ Instale as dependências
pip install -r requirements.txt

4️⃣ Configure a variável de ambiente

Crie um arquivo .env com sua chave da OpenAI:
OPENAI_API_KEY=sua_chave_aqui

5️⃣ Execute o pipeline ETL
python main.py

Observações Importantes

## A API oficial do Santander Dev Week 2023 foi descontinuada.
O projeto foi adaptado para manter o foco no fluxo ETL.
Nenhuma chave sensível é versionada no repositório.

👤 Autor

Gustavo Fernandes
Desenvolvedor de Sistemas
🔗 LinkedIn: https://www.linkedin.com/in/gustavo-fernandes-194b3a214/

