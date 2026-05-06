# WebScrapper FrenquLab - Captcha Solver

Este projeto é um webscraper desenvolvido para superar desafios de login protegidos por **reCAPTCHA v2**, utilizando uma abordagem de **Scraping Estático** (sem emulação de navegador).

## 🚀 Objetivo
Criar um webscrapper capaz de passar por uma página de login com Recaptcha realizando o login automatizado no site `https://frenqulabi.com/login` utilizando requisições HTTP diretas e integração com a API do CapMonster para resolução de captchas.

## 🛠 Tecnologias e Ferramentas
- **Python 3.13**: Linguagem base.
- **HTTPX**: Cliente HTTP para requisições assíncronas e persistência de cookies.
- **CapMonster Cloud**: Serviço de resolução de CAPTCHAs.
- **Python-dotenv**: Gerenciamento de variáveis de ambiente seguras.
- **POO (Programação Orientada a Objetos)**: Arquitetura baseada em classes e separação de responsabilidades.

## 🏗 Arquitetura do Projeto
A solução foi dividida em três módulos principais para garantir a manutenção e escalabilidade:
1.  **`solver.py`**: Gerencia a comunicação com a API do CapMonster (Criação de tarefas e Polling de resultados).
2.  **`scraper.py`**: Orquestra a sessão HTTP, gerencia headers/cookies e executa a lógica de negócio (POST de login).
3.  **`main.py`**: Ponto de entrada que coordena a execução e garante o fechamento seguro das conexões.

## ⚙️ Configuração
1.  Crie um ambiente virtual: `python -m venv venv`
2.  Ative o ambiente e instale as dependências: `pip install -r requirements.txt`
3.  Crie um arquivo `.env` na raiz com a chave de API do CapMonster:
    ```env
    CAPMONSTER_API_KEY=sua_chave_aqui
    ```

## 📈 Análises e Sugestões
Foi um prazer atuar com esse projeto e suas sugestões de melhoria são muito bem-vindas!