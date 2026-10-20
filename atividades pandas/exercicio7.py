import pandas as pd
import os

# Obtém o caminho da pasta onde este ficheiro está guardado
diretorio = os.path.dirname(__file__)

# Nome do ficheiro CSV da sua pasta
nome_ficheiro = 'HEITOR DINIZ PEREIRA GONCALVES - Automobile_data - HEITOR DINIZ PEREIRA GONCALVES - Automobile_data.csv'
caminho_csv = os.path.join(diretorio, nome_ficheiro)

# Carregar os dados
df = pd.read_csv(caminho_csv)

# Padronizar nomes de colunas (substitui traços por underscores)
df.columns = df.columns.str.strip().str.replace('-', '_')

# Calcular a média de consumo/quilometragem por fabricante
media_km = df.groupby('company')['average_mileage'].mean().sort_values(ascending=False).round(2)

print("Quilometragem média por fabricante (mpg):")
print(media_km)