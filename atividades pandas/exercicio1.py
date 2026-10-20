import pandas as pd
import os

# Localiza a pasta onde o ficheiro planilha.py está guardado
diretorio = os.path.dirname(__file__)

# Cria o caminho exato até à planilha
caminho_csv = os.path.join(diretorio, 'HEITOR DINIZ PEREIRA GONCALVES - Automobile_data - HEITOR DINIZ PEREIRA GONCALVES - Automobile_data.csv')

# Carrega e exibe os dados
df = pd.read_csv(caminho_csv)
print(df.head())