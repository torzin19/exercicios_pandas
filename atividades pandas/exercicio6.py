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

# Preencher preços nulos com a mediana para não dar erro
df['price'] = df.groupby('company')['price'].transform(lambda x: x.fillna(x.median()))

# Obter a linha do maior preço para cada montadora
carro_mais_caro_por_empresa = df.loc[df.groupby('company')['price'].idxmax()]

# Ordenar do mais caro ao mais barato
carro_mais_caro_por_empresa = carro_mais_caro_por_empresa.sort_values(by='price', ascending=False)

# Exibir colunas principais
print(carro_mais_caro_por_empresa[['company', 'body_style', 'horsepower', 'price']].to_string(index=False))