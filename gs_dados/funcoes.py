import pandas as pd

def carregar_dados():
    """Carrega os dados das fontes da Wikipedia e os retorna em um dicionário de dataframes."""
    dados = {}
    try:
        population_url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
        gdp_url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)_per_capita'
        retirement_url = 'https://en.wikipedia.org/wiki/Retirement_age#Retirement_age_by_country_and_region'
        labor_force_url = 'https://en.wikipedia.org/wiki/List_of_countries_by_labour_force'
        sector_composition_url = 'https://en.wikipedia.org/wiki/List_of_countries_by_sector_composition_of_the_labor_force'

        dados['populacao'] = pd.read_html(population_url, header=0)[0]
        dados['pib_per_capita'] = pd.read_html(gdp_url, header=0)[1]
        dados['idade_aposentadoria'] = pd.read_html(retirement_url, header=0)[0]
        dados['forca_trabalho'] = pd.read_html(labor_force_url, header=0)[0]
        dados['composicao_setores'] = pd.read_html(sector_composition_url, header=0)[0]
        print('Dados carregados com sucesso!')
        return dados
    except Exception as e:
        print(f'Erro ao carregar os dados: {e}')
        return None

def limpar_e_preparar_dados(dados):
    """Limpa e prepara os dados, unindo-os em um único DataFrame."""
    if dados is None:
        return None

    # Limpeza de cada dataframe
    pop = dados['populacao'][['Country/Territory', 'Population']].rename(columns={'Country/Territory': 'Pais', 'Population': 'Populacao'})
    pib = dados['pib_per_capita'][['Country/Territory', 'USD[4]']].rename(columns={'Country/Territory': 'Pais', 'USD[4]': 'PIB_per_capita'})
    aposentadoria = dados['idade_aposentadoria'][['Country', 'Men']].rename(columns={'Country': 'Pais', 'Men': 'Idade_Aposentadoria_Homens'})
    trabalho = dados['forca_trabalho'][['Country', 'Labour force']].rename(columns={'Country': 'Pais', 'Labour force': 'Forca_Trabalho'})
    setores = dados['composicao_setores'][['Country', 'Agriculture (%)', 'Industry (%)', 'Services (%)']].rename(columns={'Country': 'Pais', 'Agriculture (%)': 'Agricultura_%', 'Industry (%)': 'Industria_%', 'Services (%)': 'Servicos_%'})

    # Merge dos dataframes
    df = pd.merge(pop, pib, on='Pais', how='inner')
    df = pd.merge(df, aposentadoria, on='Pais', how='inner')
    df = pd.merge(df, trabalho, on='Pais', how='inner')
    df = pd.merge(df, setores, on='Pais', how='inner')

    # Limpeza final
    df['PIB_per_capita'] = df['PIB_per_capita'].astype(str).str.replace(r'\D', '', regex=True).astype(float)
    df['Forca_Trabalho'] = df['Forca_Trabalho'].astype(str).str.replace(r'\D', '', regex=True).astype(float)
    df = df.apply(pd.to_numeric, errors='coerce')
    df.dropna(inplace=True)

    return df.reset_index(drop=True)

def apresenta_dado(df, nome_dado):
    """Retorna uma série com os dados de uma coluna específica."""
    if nome_dado in df.columns:
        return df[['Pais', nome_dado]]
    else:
        return f'Dado \'{nome_dado}\' não encontrado.'

def apresenta_pais(df, nome_pais):
    """Retorna um dicionário com os dados de um país específico."""
    if nome_pais in df['Pais'].values:
        return df[df['Pais'] == nome_pais].to_dict('records')[0]
    else:
        return f'País \'{nome_pais}\' não encontrado.'

def calcula_media_de_dado(df, nome_dado):
    """Calcula a média de uma coluna de dados."""
    if nome_dado in df.columns and pd.api.types.is_numeric_dtype(df[nome_dado]):
        return df[nome_dado].mean()
    else:
        return f'Não foi possível calcular a média para \'{nome_dado}\''.'

def calcula_variancia_de_dado(df, nome_dado):
    """Calcula a variância de uma coluna de dados."""
    if nome_dado in df.columns and pd.api.types.is_numeric_dtype(df[nome_dado]):
        return df[nome_dado].var()
    else:
        return f'Não foi possível calcular a variância para \'{nome_dado}\''.'

def calcula_media_ponderada_de_dado(df, nome_dado, peso):
    """Calcula a média ponderada de uma coluna de dados."""
    if nome_dado in df.columns and peso in df.columns and pd.api.types.is_numeric_dtype(df[nome_dado]) and pd.api.types.is_numeric_dtype(df[peso]):
        return (df[nome_dado] * df[peso]).sum() / df[peso].sum()
    else:
        return f'Não foi possível calcular a média ponderada para \'{nome_dado}\' com peso \'{peso}\''.'

def calcula_correlacao(df, dado1, dado2):
    """Calcula a correlação entre duas colunas de dados."""
    if dado1 in df.columns and dado2 in df.columns and pd.api.types.is_numeric_dtype(df[dado1]) and pd.api.types.is_numeric_dtype(df[dado2]):
        return df[dado1].corr(df[dado2])
    else:
        return f'Não foi possível calcular a correlação entre \'{dado1}\' e \'{dado2}\''.'
