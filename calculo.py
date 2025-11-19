import pandas as pd

def carregar_dados_locais():
    """Carrega os dados dos arquivos CSV locais na pasta gs_dados/."""
    dados = {}
    try:
        dados['paises'] = pd.read_csv('gs_dados/countries.csv')
        dados['populacao'] = pd.read_csv('gs_dados/population.csv')
        dados['servicos'] = pd.read_csv('gs_dados/services_percent_of_gdp.csv')
        
        print("Arquivos CSV locais carregados com sucesso!")
        return dados
    except FileNotFoundError as e:
        print(f"Erro ao carregar arquivos CSV: {e}. Verifique se os arquivos estão na pasta gs_dados/.")
        return None

def processar_e_unificar_dados(dados_brutos):
    """
    Processa os dados DDF do Gapminder, pega o ano mais recente de cada indicador
    para cada país e unifica tudo em um único DataFrame.
    """
    if dados_brutos is None:
        return None

    try:
        paises = dados_brutos['paises'][['country', 'name']].rename(columns={'country': 'geo', 'name': 'Pais'})

        def get_latest_data(df, nome_valor):
            if 'time' not in df.columns or 'geo' not in df.columns:
                if nome_valor is None:
                    return df
                else:
                    raise ValueError(f"O DataFrame para '{nome_valor}' não contém as colunas 'time' ou 'geo'.")
            
            df_recente = df.sort_values('time', ascending=False).drop_duplicates('geo')
            df_recente = df_recente[['geo', nome_valor]]
            return df_recente

        pop_recente = get_latest_data(dados_brutos['populacao'], 'total_population_with_projections')
        pop_recente = pop_recente.rename(columns={'total_population_with_projections': 'Populacao'})
        
        serv_recente = get_latest_data(dados_brutos['servicos'], 'services_percent_of_gdp')
        serv_recente = serv_recente.rename(columns={'services_percent_of_gdp': 'Servicos_%'})

        df = pd.merge(paises, pop_recente, on='geo', how='inner')
        df = pd.merge(df, serv_recente, on='geo', how='inner')

        df = df[['Pais', 'Populacao', 'Servicos_%']].copy()
        df.dropna(inplace=True)
        df['Populacao'] = df['Populacao'].astype(int)
        df.reset_index(drop=True, inplace=True)

        print(f"Dados processados e unificados. Total de {len(df)} países no dataset final.")
        return df
        
    except Exception as e:
        print(f"Erro ao processar e unificar os dados: {e}")
        return None

def calcula_media(df, nome_coluna):
    """Calcula a média de uma coluna de dados específica."""
    if nome_coluna in df.columns and pd.api.types.is_numeric_dtype(df[nome_coluna]):
        return df[nome_coluna].mean()
    else:
        return f"Não foi possível calcular a média para '{nome_coluna}'. Coluna não encontrada ou não é numérica."

def calcula_variancia(df, nome_coluna):
    """Calcula a variância de uma coluna de dados específica."""
    if nome_coluna in df.columns and pd.api.types.is_numeric_dtype(df[nome_coluna]):
        return df[nome_coluna].var()
    else:
        return f"Não foi possível calcular a variância para '{nome_coluna}'. Coluna não encontrada ou não é numérica."

def calcula_media_ponderada(df, coluna_valor, coluna_peso):
    """
    Calcula a média ponderada de uma coluna de dados específica.
    'coluna_peso' especifica a coluna a ser usada como pesos.
    """
    if (coluna_valor in df.columns and coluna_peso in df.columns and
        pd.api.types.is_numeric_dtype(df[coluna_valor]) and pd.api.types.is_numeric_dtype(df[coluna_peso])):
        
        if (df[coluna_peso] <= 0).any():
            print(f"Aviso: '{coluna_peso}' contém valores não positivos. Estes serão tratados como peso zero.")
            temp_df = df[df[coluna_peso] > 0].copy()
            if temp_df.empty:
                return "Não é possível calcular a média ponderada: todos os pesos são não positivos."
            return (temp_df[coluna_valor] * temp_df[coluna_peso]).sum() / temp_df[coluna_peso].sum()
        
        return (df[coluna_valor] * df[coluna_peso]).sum() / df[coluna_peso].sum()
    else:
        return f"Não foi possível calcular a média ponderada para '{coluna_valor}' com peso '{coluna_peso}'. Colunas não encontradas ou não são numéricas."

def calcula_correlacao(df, coluna1, coluna2):
    """Calcula a correlação entre duas colunas de dados específicas."""
    if (coluna1 in df.columns and coluna2 in df.columns and
        pd.api.types.is_numeric_dtype(df[coluna1]) and pd.api.types.is_numeric_dtype(df[coluna2])):
        return df[coluna1].corr(df[coluna2])
    else:
        return f"Não foi possível calcular a correlação entre '{coluna1}' e '{coluna2}'. Colunas não encontradas ou não são numéricas."

def apresenta_dados_pais(df, nome_pais):
    """Retorna um dicionário com todos os dados disponíveis para um país específico."""
    if nome_pais in df['Pais'].values:
        dict_pais = df[df['Pais'] == nome_pais].to_dict('records')
        if dict_pais:
            return dict_pais[0]
    return f"País '{nome_pais}' não encontrado."

def apresenta_coluna_dados(df, nome_coluna):
    """Retorna uma Série com os dados de uma coluna específica, incluindo o nome do país."""
    if nome_coluna in df.columns:
        return df[['Pais', nome_coluna]]
    else:
        return f"Coluna '{nome_coluna}' não encontrada."
