import pandas as pd
import os

# Obtém o caminho da pasta onde este ficheiro está guardado
diretorio = os.path.dirname(__file__)

# Nome do ficheiro que está guardado no seu projeto
nome_ficheiro = 'HEITOR DINIZ PEREIRA GONCALVES - Automobile_data - HEITOR DINIZ PEREIRA GONCALVES - Automobile_data.csv'
caminho_csv = os.path.join(diretorio, nome_ficheiro)

# Carregar os dados
df = pd.read_csv(caminho_csv)

# Padronizar nomes de colunas (substitui traços por underscores)
df.columns = df.columns.str.strip().str.replace('-', '_')

# Ordenar por preço em ordem crescente
df_ordenado = df.sort_values(by='price', ascending=True)

# Exibir os resultados
print(df_ordenado[['company', 'body_style', 'horsepower', 'average_mileage', 'price']].to_string(index=False))
