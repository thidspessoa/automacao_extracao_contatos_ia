# 🤖 Automação de Extração e Persistência de Contatos

Este projeto é uma **automação desenvolvida em Python** com foco na **captação estruturada de contatos a partir de landing-pages e perfis do instagram**, organizada como parte do projeto *Projeto automação captação de contatos e mensagem*.

Na versão atual (**release 1.0.0**), o escopo do projeto contempla **exclusivamente a extração e persistência de dados em planilhas Excel**, servindo como base sólida para futuras evoluções envolvendo **mensageria automatizada**.

O objetivo principal é criar uma solução **modular, escalável e orientada a automação**, permitindo que novas etapas (como validação, enriquecimento e envio de mensagens) sejam adicionadas de forma incremental.

---

## 📦 Tecnologias

* `Python` — linguagem principal do projeto
* `Selenium` — automação de navegação e coleta de dados
* `Pandas` — tratamento e estruturação dos dados
* `OpenPyXL / Excel` — persistência dos dados extraídos
* `Virtualenv` — isolamento do ambiente de desenvolvimento
* `Git / GitHub / Github CLI` — versionamento e controle de código
* `Gemini API` — Para limpeza e estruturação dos dados brutos extraídos da web

---

## 🧩 Features

Funcionalidades disponíveis **na versão 1.0.0**:

* **Automação de navegação web** para coleta de informações de landing pages e perfis do instagram
* **Extração estruturada de dados de contato**
* **Tratamento e normalização dos dados coletados**
* **Persistência em arquivo Excel**, com organização por colunas
* **Estrutura de código modular**, preparada para evolução

Funcionalidades **planejadas para próximas versões**:

* Integração com N8N para **mensageria (WhatsApp / APIs)**
* Validação e enriquecimento de contatos
* Persistência alternativa (banco de dados)
* Orquestração via API (FastAPI)
* Execução agendada e/ou em containers do N8N (Docker)

---

## 🧠 Arquitetura do Projeto

O projeto foi estruturado com foco em **clareza, separação de responsabilidades e manutenibilidade**.

A automação segue um fluxo lógico:

1. Inicialização do ambiente e do WebDriver
2. Acesso controlado à plataforma alvo
3. Extração dos dados relevantes
4. Tratamento e padronização das informações
5. Persistência final em Excel

Essa arquitetura permite que novas etapas sejam adicionadas ao pipeline sem impacto direto no núcleo existente.

---

## 📚 O Que Aprendi

Este projeto consolidou conhecimentos importantes no contexto de **automação e back-end em python**:

### 🧩 Automação Web

* Uso avançado do Selenium
* Gerenciamento de sessões e perfis de navegador
* Tratamento de erros e falhas de carregamento

### 📊 Manipulação de Dados

* Estruturação de dados com Pandas
* Normalização de informações inconsistentes
* Tratamento de dados brutos raspados da web utilizando Inteligência Artifical
* Exportação confiável para Excel

### 🏗️ Organização de Código

* Separação por camadas e responsabilidades (extração, processamento, persistência)
* Código preparado para escalar
* Base sólida para integração com APIs
* Orientação a Objetos na pratica
* Type hints para tipagem de dados

### 📈 Visão de Produto

* Construção incremental por versões
* Definição clara de escopo por release
* Planejamento de features futuras sem comprometer estabilidade

---

## 💭 Próximos Passos / Melhorias Futuras

* Implementar módulo de **mensageria automatizada com orquestração em N8N**
* Criar API para comunicação com o N8N
* Persistência em banco de dados relacional
* Logs estruturados e monitoramento
* Containerização com Docker

---

## 🚦 Rodando o Projeto Localmente

Para executar o projeto em ambiente local:

1. Clone o repositório:

   ```bash
   git clone <url-do-repositorio>
   ```
2. Crie e ative o ambiente virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```
4. Execute o projeto:

   ```bash
   python -m src.main
   ```

---

## 🏷️ Versionamento

Este projeto segue **Versionamento Semântico (SemVer)**:

* `1.0.0` — Extração e persistência de contatos em Excel

Novas versões serão lançadas conforme a evolução do pipeline de automação.
