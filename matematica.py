import numpy as np

def media(valores):
    return np.mean(valores)

def variancia_populacional(valores):
    return np.var(valores, ddof=0)

def variancia_amostral(valores):
    return np.var(valores, ddof=1)

def covariancia(valores1, valores2):
    return np.cov(valores1, valores2)[0, 1]

def desvio_padrao(valores):
    return np.std(valores, ddof=1)

def correlacao(valores1, valores2):
    # np.corrcoef retorna uma matriz de correlação
    # A correlação entre as duas variáveis está no elemento [0, 1]
    matriz_corr = np.corrcoef(valores1, valores2)
    return matriz_corr[0, 1]
