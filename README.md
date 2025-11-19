# GS Python & Cálculo - Análise sobre o Futuro do Trabalho

Este projeto foi desenvolvido para a Global Solution (GS) e aborda o tema "O Futuro do Trabalho: A Era da Requalificação Contínua". A análise combina conceitos de programação em Python para análise de dados e de Cálculo para modelagem matemática.

## 📝 Descrição

O objetivo deste trabalho é analisar fatores socioeconômicos de diversos países e conectá-los com a necessidade de aprendizado contínuo na força de trabalho do futuro. Para isso, o projeto realiza duas análises principais:

1.  **Análise de Dados (Python):** Utiliza dados de população e da participação do setor de serviços no PIB para calcular um **Índice de Prontidão para o Futuro (IPF)**. Funções estatísticas como média, variância, média ponderada e correlação são aplicadas para extrair insights dos dados.
2.  **Modelagem Matemática (Cálculo):** Modela uma **Curva de Aprendizado** usando uma função de crescimento exponencial. A velocidade e o acúmulo de conhecimento são explorados através de derivadas e integrais. A taxa de aprendizado no modelo é dinamicamente ajustada pelo IPF de cada país, conectando a estrutura econômica à capacidade de requalificação.

O projeto busca alinhar as conclusões com os **Objetivos de Desenvolvimento Sustentável (ODS)** 4 (Educação de Qualidade) e 8 (Trabalho Decente e Crescimento Econômico) da ONU.

## 📂 Estrutura do Projeto

- `analise_dados.ipynb`: Notebook Jupyter contendo a análise completa, desde o carregamento e processamento dos dados até a modelagem matemática e as visualizações interativas.
- `funcoes.py`: Módulo Python que centraliza as funções para carregamento, processamento de dados e os cálculos estatísticos.
- `gs_dados/`: Diretório que armazena os datasets em formato `.csv` utilizados na análise.
- `README.md`: Este arquivo.

## 🚀 Como Executar

Para visualizar e interagir com a análise, siga os passos abaixo:

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/Caioncaminha/gspythoncalculo
    cd gspythoncalculo
    ```

2.  **Crie e ative um ambiente virtual:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

    _(No Windows, use `\.venv\Scripts\activate`)_

3.  **Instale as dependências:**
    Crie um arquivo `requirements.txt` com o conteúdo abaixo e execute o comando `pip install -r requirements.txt`.

    ```
    pandas
    matplotlib
    ipywidgets
    numpy
    jupyterlab
    ```

4.  **Inicie o Jupyter Lab:**

    ```bash
    jupyter lab
    ```

5.  No navegador, abra o arquivo `analise_dados.ipynb` e execute as células.

## 🛠️ Dependências

As principais bibliotecas utilizadas no projeto são:

- `pandas`
- `numpy`
- `matplotlib`
- `ipywidgets`
- `jupyterlab`

Certifique-se de instalá-las usando o arquivo `requirements.txt` conforme as instruções acima.

## 👥Integrantes

- Caio Nascimento Caminha - RM564789
- Giovana Rosatti Parreira - RM562275
