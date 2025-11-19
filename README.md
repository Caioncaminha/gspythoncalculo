# GS Python & Cálculo - Análise sobre o Futuro do Trabalho

## Introdução

Este projeto foi desenvolvido para a Global Solution (GS) e aborda o tema "O Futuro do Trabalho: A Era da Requalificação Contínua". A análise combina conceitos de programação em Python para análise de dados e de Cálculo para modelagem matemática.

## Visão Geral do Projeto

Este projeto oferece uma abordagem multidisciplinar para entender tendências globais e o processo de aprendizado contínuo. Combinando a análise de dados socioeconômicos de diversos países com conceitos matemáticos de cálculo, exploramos como diferentes economias se posicionam para o futuro e como o conhecimento é adquirido e aprimorado ao longo do tempo.

Em termos simples, o projeto busca responder:

1.  **Como países se comparam** em termos de indicadores chave (população, participação de serviços no PIB) ao longo do tempo?
2.  **Podemos prever a capacidade de "aprendizado"** (adaptação a novas realidades e tecnologias) de um país com base em sua estrutura econômica?

## Funcionalidades Principais

- **Coleta e Processamento de Dados:** Extrai e organiza dados históricos e recentes de população e a porcentagem de serviços no Produto Interno Bruto (PIB) de diferentes nações.
- **Análise Estatística:** Calcula métricas importantes como média, variância e correlação para entender as relações entre os dados.
- **Índice de Prontidão para o Futuro (IPF):** Um indicador desenvolvido no projeto que reflete a capacidade de uma economia de se adaptar a mudanças, baseado na relevância do setor de serviços no seu PIB.
- **Modelagem da Curva de Aprendizado:** Utiliza princípios de cálculo (limites, derivadas) para simular o processo de aquisição de conhecimento, mostrando como o "IPF" de um país pode influenciar sua velocidade de aprendizado e desenvolvimento.

## Como Usar

Para explorar o projeto, siga os passos abaixo:

### 1. Instalação

Certifique-se de ter o Python instalado. Em seguida, instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

### 2. Execução do Notebook Interativo

Abra o arquivo `analise_dados.ipynb` e execute as células sequencialmente para ver a análise em ação, incluindo gráficos interativos que mostram a curva de aprendizado de diferentes países.

### 3. Análise de Séries Temporais via Script

Para realizar análises mais detalhadas sobre a série histórica de dados de países específicos, você pode executar o script `funcoes_basicas.py` diretamente. Este script inclui exemplos de como obter dados históricos, calcular médias, variâncias e correlações para um país selecionado.

```bash
python funcoes_basicas.py
```

## Estrutura do Projeto

- `analise_dados.ipynb`: O notebook principal para a análise exploratória, modelagem da curva de aprendizado e visualizações interativas.
- `calculo.py`: Contém funções para carregar, processar e unificar dados recentes, além de funções para cálculo de médias, variâncias e correlações para um _snapshot_ atualizado dos dados.
- `funcoes_basicas.py`: Fornece funções para carregar e processar dados históricos, além de funções para análises estatísticas específicas para a _série temporal_ de cada país.
- `matematica.py`: Um módulo utilitário com implementações puras de funções matemáticas como média, variância, covariância e correlação, usadas pelas outras funções de análise.
- `gs_dados/`: Pasta que armazena os arquivos CSV com os dados brutos de países, população e percentual de serviços no PIB.
- `requirements.txt`: Lista todas as bibliotecas Python necessárias para o projeto.

## Conexão com os Objetivos de Desenvolvimento Sustentável (ODS)

Este projeto se alinha a importantes Objetivos de Desenvolvimento Sustentável da ONU:

- **ODS 4: Educação de Qualidade:** A modelagem da curva de aprendizado destaca a importância da educação contínua e da adaptabilidade para o desenvolvimento individual e nacional.
- **ODS 8: Trabalho Decente e Crescimento Econômico:** A análise do IPF e sua relação com a velocidade de aprendizado sugere como a estrutura econômica de um país e a capacidade de sua força de trabalho em se adaptar são cruciais para um crescimento econômico sustentável e a criação de empregos de qualidade.

## Conclusão

Através da combinação de análise de dados e modelagem matemática, este projeto ilustra a intrínseca relação entre a estrutura econômica de uma nação e sua capacidade de aprendizado e adaptação. Ao priorizar estratégias que fomentem o aprendizado contínuo, governos e instituições podem construir forças de trabalho mais resilientes e preparadas para os desafios do futuro.

## 👥Integrantes

- Caio Nascimento Caminha - RM564789
- Giovana Rosatti Parreira - RM562275
