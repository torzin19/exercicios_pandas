import pandas as pd
import os

# Define o caminho exato da pasta onde o script está salvo
diretorio = os.path.dirname(__file__)

# Nome do ficheiro que está na sua pasta à esquerda
nome_ficheiro = 'HEITOR DINIZ PEREIRA GONCALVES - Automobile_data - HEITOR DINIZ PEREIRA GONCALVES - Automobile_data.csv'
caminho_csv = os.path.join(diretorio, nome_ficheiro)

# Carregar os dados
df = pd.read_csv(caminho_csv)

# Trata a coluna de preço se houver nulos
df['price'] = df.groupby('company')['price'].transform(lambda x: x.fillna(x.median()))

# 1. Montadora do veículo mais caro
mais_caro = df.loc[df['price'].idxmax()]
print(f"Carro mais caro: {mais_caro['company']} - ${mais_caro['price']:,.2f}")

# 2. Montadora com a maior média de preço
media_marca = df.groupby('company')['price'].mean().sort_values(ascending=False)
print(f"\nMontadora com maior preço médio: {media_marca.index[0]} - ${media_marca.iloc[0]:,.2f}")