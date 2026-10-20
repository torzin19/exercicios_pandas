import pandas as pd
import os

# Obtém a pasta onde este ficheiro está guardado
diretorio = os.path.dirname(__file__)

# Nome do ficheiro que está na sua pasta
nome_ficheiro = 'HEITOR DINIZ PEREIRA GONCALVES - Automobile_data - HEITOR DINIZ PEREIRA GONCALVES - Automobile_data.csv'
caminho_csv = os.path.join(diretorio, nome_ficheiro)

# Carregar os dados
df = pd.read_csv(caminho_csv)

# Contar a quantidade de carros por empresa
contagem = df['company'].value_counts()

print("Total de carros por empresa:")
print(contagem)