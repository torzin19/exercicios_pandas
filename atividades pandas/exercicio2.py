import pandas as pd
import os

# Obtém a pasta onde o ficheiro exercicio2.py está guardado
diretorio = os.path.dirname(__file__)

# Define o caminho do arquivo (usa o original ou o limpo, se existir)
caminho_csv = os.path.join(diretorio, 'HEITOR DINIZ PEREIRA GONCALVES - Automobile_data - HEITOR DINIZ PEREIRA GONCALVES - Automobile_data.csv')

# Carregar os dados
df = pd.read_csv(caminho_csv)

# Se existirem nomes de colunas com hífen, ajusta para o código não falhar
df.columns = df.columns.str.strip().str.replace('-', '_')

# Ordenar por preço em ordem crescente
df_ordenado = df.sort_values(by='price', ascending=True)

# Exibir os resultados
print(df_ordenado[['company', 'body_style', 'horsepower', 'average_mileage', 'price']].to_string(index=False))