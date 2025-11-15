# Resumo do Projeto - Análise de Dados Socioeconômicos e Curva de Aprendizagem

Este projeto foi desenvolvido para atender aos requisitos das matérias de Python e Cálculo, abordando a análise de dados sobre o mercado de trabalho e a modelagem matemática da curva de conhecimento.

## Tópicos Principais

### Parte 1: Análise de Dados com Python

*   **Coleta de Dados:** Os dados foram coletados de fontes da Wikipedia, utilizando a biblioteca `pandas` para extrair as tabelas diretamente das páginas HTML. As fontes utilizadas foram:
    *   População: [List of countries and dependencies by population](https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population)
    *   PIB per capita: [List of countries by GDP (nominal) per capita](https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)_per_capita)
    *   Idade de Aposentadoria: [Retirement age](https://en.wikipedia.org/wiki/Retirement_age#Retirement_age_by_country_and_region)
    *   Força de Trabalho: [List of countries by labour force](https://en.wikipedia.org/wiki/List_of_countries_by_labour_force)
    *   Composição da Força de Trabalho por Setor: [List of countries by sector composition of the labor force](https://en.wikipedia.org/wiki/List_of_countries_by_sector_composition_of_the_labor_force)

*   **Limpeza e Preparação dos Dados:** Os dados brutos foram limpos e pré-processados para garantir a consistência e a qualidade. Isso incluiu a renomeação de colunas, a conversão de tipos de dados, o tratamento de valores ausentes e a união de diferentes fontes de dados em um único DataFrame.

*   **Funções de Análise:** Foram implementadas as seguintes funções para análise dos dados:
    *   `apresenta_dado(df, nome_dado)`: Exibe uma coluna específica do DataFrame.
    *   `apresenta_pais(df, nome_pais)`: Exibe todos os dados de um país específico.
    *   `calcula_media_de_dado(df, nome_dado)`: Calcula a média de uma coluna.
    *   `calcula_variancia_de_dado(df, nome_dado)`: Calcula a variância de uma coluna.
    *   `calcula_media_ ponderada_de_dado(df, nome_dado, peso)`: Calcula a média ponderada.
    *   `calcula_correlacao(df, dado1, dado2)`: Calcula a correlação entre duas colunas.

### Parte 2: Modelagem da Curva de Aprendizagem com Cálculo

*   **Função de Conhecimento:** Foi utilizada a função `K(t) = 100 * (1 - e**(-0.2*t))` para modelar o acúmulo de conhecimento ao longo do tempo.

*   **Análise da Função:**
    *   **Limite:** O limite da função quando o tempo tende ao infinito foi calculado, representando o nível máximo de conhecimento.
    *   **Derivada:** A derivada da função foi calculada para representar a velocidade do aprendizado.
    *   **Gráficos:** Foram gerados gráficos da função de conhecimento e de sua derivada para visualizar a curva de aprendizagem e o ritmo de aprendizado.

*   **Conexão com os ODS:** A análise foi conectada aos Objetivos de Desenvolvimento Sustentável (ODS) 4 (Educação de Qualidade) e 8 (Trabalho Decente e Crescimento Econômico), destacando a importância do aprendizado contínuo e da requalificação profissional.

## Ordem de Prioridade

1.  **Funcionalidade do Código:** Garantir que todo o código Python funcione corretamente e produza os resultados esperados.
2.  **Atendimento aos Requisitos:** Cumprir todos os requisitos especificados no arquivo `contexto.md`, tanto para a parte de Python quanto para a de Cálculo.
3.  **Qualidade do Código:** Escrever um código limpo, bem documentado e organizado.
4.  **Análise e Interpretação:** Fornecer análises e interpretações claras e coerentes dos resultados, tanto na análise de dados quanto na modelagem da curva de aprendizagem.
5.  **Clareza da Apresentação:** Apresentar os resultados de forma clara e organizada no Jupyter Notebook e no arquivo de resumo.
