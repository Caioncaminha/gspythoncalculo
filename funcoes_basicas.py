import pandas as pd
import numpy as np
import random
from matematica import variancia_amostral, media, correlacao, variancia_populacional

def carregar_dados_csv():
    """
    Carrega os dados de população, serviços e países de arquivos CSV.
    """
    try:
        population = pd.read_csv('gs_dados/population.csv', header=None, names=['geo', 'year', 'population'])
        services = pd.read_csv('gs_dados/services_percent_of_gdp.csv', header=None, names=['geo', 'year', 'services_percent_of_gdp'])
        all_country_data = pd.read_csv('gs_dados/countries.csv', header=0)
        return population, services, all_country_data
    except FileNotFoundError as e:
        print(f"Erro Crítico: Não foi possível encontrar o arquivo: {e}.")
        return None, None, None

def processar_dados(population, services, all_country_data):
    """
    Processa e une os DataFrames de população, serviços e países.
    """
    if population is None or services is None or all_country_data is None:
        return None

    # A coluna 'country' na verdade contém o código 'geo', e 'name' contém o nome completo.
    if 'country' in all_country_data.columns and 'name' in all_country_data.columns:
        country_map = all_country_data[['country', 'name']].copy()
        country_map.rename(columns={'country': 'geo', 'name': 'country_name'}, inplace=True)
    else:
        # Fallback caso a estrutura do arquivo mude inesperadamente
        print("Aviso: Estrutura do 'countries.csv' não é a esperada. Nomes completos podem não aparecer.")
        country_map = pd.DataFrame(columns=['geo', 'country_name'])

    # --- Tratamento de Tipos e Limpeza ---
    for df in [population, services, country_map]:
        if 'geo' in df.columns:
            df['geo'] = df['geo'].str.strip()
    
    for df in [population, services]:
        df['year'] = pd.to_numeric(df['year'], errors='coerce')
    
    population['population'] = pd.to_numeric(population['population'], errors='coerce')
    services['services_percent_of_gdp'] = pd.to_numeric(services['services_percent_of_gdp'], errors='coerce')
    
    for df in [population, services]:
        df.dropna(subset=['year', 'geo'], inplace=True)
    
    population['year'] = population['year'].astype(int)
    services['year'] = services['year'].astype(int)

    # --- Merge dos Dados ---
    df_merged = pd.merge(population, services, on=['geo', 'year'], how='inner')
    
    if not country_map.empty:
        df_merged = pd.merge(df_merged, country_map, on='geo', how='left')
        # Usa o nome completo do país como índice. Se não houver, usa o código 'geo'.
        df_merged['country_name'] = df_merged['country_name'].fillna(df_merged['geo'])
        df_merged.set_index('country_name', inplace=True)
    else:
        df_merged.set_index('geo', inplace=True)

    if df_merged.empty:
        print("Erro: DataFrame vazio após todos os merges. Verifique os arquivos de dados.")
        return None
        
    return df_merged

def carregar_e_processar_dados():
    """
    Carrega os dados de CSVs, trata os tipos de dados, une as tabelas
    e retorna um DataFrame completo com a série histórica por país.
    """
    try:
        population, services, all_country_data = carregar_dados_csv()
        return processar_dados(population, services, all_country_data)
    except Exception as e:
        print(f"Ocorreu um erro inesperado durante o processamento dos dados: {e}")
        return None

# --- Funções de Análise ---

def apresenta_dados_pais(dataframe, pais):
    """
    Recebe um nome de um país e retorna todos os dados históricos para ele.
    """
    if pais in dataframe.index:
        return dataframe.loc[[pais]]
    else:
        raise ValueError(f"País '{pais}' não encontrado.")

def calcula_media_por_pais(dataframe, pais, dado):
    """
    Calcula a média de um dado para um país específico ao longo do tempo.
    """
    if pais in dataframe.index:
        dados_pais = dataframe.loc[[pais]]
        if dados_pais.empty:
            return f"Não há dados disponíveis para calcular a média para o país '{pais}'."
        return media(dados_pais[dado])
    return f"Não foi possível encontrar o país '{pais}' para calcular a média."

def calcula_variancia_por_pais(dataframe, pais, dado):
    """
    Calcula a variância de um dado para um país específico ao longo do tempo.
    A variância não pode ser calculada com menos de 2 pontos de dados.
    """
    if pais in dataframe.index:
        dados_pais = dataframe.loc[[pais]]
        # A variância requer pelo menos 2 pontos de dados.
        if dados_pais.shape[0] < 2:
            return f"Não há dados suficientes para calcular a variância para o país '{pais}' (mínimo de 2 pontos necessários)."
        
        if dado == 'population':
            return variancia_populacional(dados_pais[dado])
        else:
            return variancia_amostral(dados_pais[dado])
    return f"Não foi possível encontrar o país '{pais}' para calcular a variância."

def calcula_correlacao_por_pais(dataframe, pais, dado1, dado2):
    """
    Calcula a correlação entre dois dados para um país específico ao longo do tempo.
    A correlação não pode ser calculada com menos de 2 pontos de dados.
    """
    if pais in dataframe.index:
        dados_pais = dataframe.loc[[pais]]
        # A correlação requer pelo menos 2 pontos de dados.
        if dados_pais.shape[0] < 2:
            return f"Não há dados suficientes para calcular a correlação para o país '{pais}' (mínimo de 2 pontos necessários)."
        return correlacao(dados_pais[dado1], dados_pais[dado2])
    return f"Não foi possível encontrar o país '{pais}' para calcular a correlação."

def formatar_numero_br(numero):
    """Formata um número para o padrão brasileiro (ex: 1.234.567,89)."""
    if not isinstance(numero, (int, float)):
        return numero
    return f"{numero:,.2f}".replace('.', 'TEMP').replace(',', '.').replace('TEMP', ',')

# --- Bloco de Execução de Exemplo ---

if __name__ == "__main__":
    print("--- Carregando e processando dados... ---")
    dados_completos = carregar_e_processar_dados()

    if dados_completos is None or dados_completos.empty:
        print("\nErro: Não foi possível carregar os dados para os testes.")
    else:
        print("\n--- Testando funcoes_basicas.py com exemplos aleatórios por país ---")
        


        # --- Configuração para Aleatorização ---
        lista_paises = dados_completos.index.unique().tolist()
        colunas_numericas = ['population', 'services_percent_of_gdp']
        
        pais_aleatorio = random.choice(lista_paises)
        dado_aleatorio = random.choice(colunas_numericas)
        
        print(f"\nPaís aleatório escolhido: '{pais_aleatorio}'")
        print(f"Dado aleatório escolhido para média e variância: '{dado_aleatorio}'")
        
        # --- Chamada das Funções ---

        # Exemplo 1: Apresenta dados históricos de um país aleatório
        print(f"\n=== Alguns dados históricos de '{pais_aleatorio}'  ===")
        try:
            dados_historicos = apresenta_dados_pais(dados_completos, pais_aleatorio)
        
            # Cria uma cópia para não alterar o dataframe original
            df_formatado = dados_historicos.tail(5).copy()
            
            # Arredonda 'services_percent_of_gdp' para cima
            df_formatado['services_percent_of_gdp'] = (np.ceil(df_formatado['services_percent_of_gdp'] * 100) / 100)
            
            # Aplica a formatação BR
            df_formatado['population'] = df_formatado['population'].apply(lambda x: formatar_numero_br(x).split(',')[0]) # Remove decimais da população
            df_formatado['services_percent_of_gdp'] = df_formatado['services_percent_of_gdp'].apply(formatar_numero_br)
            
            # --- Impressão formatada da tabela ---
            col_year_width = 10
            col_pop_width = 25
            col_services_width = 30
            padding = 4 # Espaços extras entre as colunas
            
            # Imprime o cabeçalho
            print(f"{'Ano':<{col_year_width}} {'População':<{col_pop_width}} {'Serviços (% PIB)':<{col_services_width}}")
            print("-" * (col_year_width + col_pop_width + col_services_width + padding * 2))
            
            # Imprime as linhas de dados
            for _, row in df_formatado.iterrows():
                print(f"{row['year']:<{col_year_width}} {row['population']:<{col_pop_width}} {row['services_percent_of_gdp']:<{col_services_width}}")
                
            # --- Fim da impressão formatada ---
        except ValueError as e:
            print(e)

        # Exemplo 2: Calcula média de um dado para o país aleatório
        print(f"\n=== Média de '{dado_aleatorio}' para '{pais_aleatorio}' ao longo do tempo ===")
        media_calculada = calcula_media_por_pais(dados_completos, pais_aleatorio, dado_aleatorio)
        if isinstance(media_calculada, (int, float)):
            print(f"Média: {formatar_numero_br(media_calculada)}")
        else:
            print(media_calculada)

        # Exemplo 3: Calcula variância de um dado para o país aleatório
        print(f"\n=== Variância de '{dado_aleatorio}' para '{pais_aleatorio}' ao longo do tempo ===")
        variancia_calculada = calcula_variancia_por_pais(dados_completos, pais_aleatorio, dado_aleatorio)
        if isinstance(variancia_calculada, (int, float)):
            print(f"Variância: {formatar_numero_br(variancia_calculada)}")
        else:
            print(variancia_calculada)
            
        # Exemplo 4: Calcula correlação entre população e serviços para o país aleatório
        print(f"\n=== Correlação entre 'population' e 'services_percent_of_gdp' para '{pais_aleatorio}' ===")
        resultado_correlacao = calcula_correlacao_por_pais(dados_completos, pais_aleatorio, 'population', 'services_percent_of_gdp')
        if isinstance(resultado_correlacao, (int, float)):
             print(f"Correlação: {formatar_numero_br(resultado_correlacao)}")
        else:
            print(resultado_correlacao)
