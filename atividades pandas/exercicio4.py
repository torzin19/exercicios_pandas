import pandas as pd
import os

# Obtém a pasta onde este ficheiro está guardado
diretorio = os.path.dirname(__file__)

# Nome correto do ficheiro CSV da sua pasta
nome_ficheiro = 'HEITOR DINIZ PEREIRA GONCALVES - Automobile_data - HEITOR DINIZ PEREIRA GONCALVES - Automobile_data.csv'
caminho_csv = os.path.join(diretorio, nome_ficheiro)

# Carregar o conjunto de dados
df = pd.read_csv(caminho_csv)

# Filtrar os carros da Toyota
toyota_df = df[df['company'] == 'toyota']

# Imprimir todos os detalhes
print(toyota_df.to_string(index=False))