import pandas as pd

# 1. Definir os dicionários
GermanCars = {
    'Company': ['FORD', 'MERCEDES', 'BMW', 'AUDI'],
    'PRICE': [23845, 135925, 171995, 71400]
}

JapaneseCars = {
    'company': ['TOYOTA', 'HONDA', 'NISSAN', 'MITSUBISHI'],
    'PRICE': [29995, 23600, 61500, 58900]
}

# 2. Criar os DataFrames
df_german = pd.DataFrame(GermanCars)
df_japanese = pd.DataFrame(JapaneseCars)

print("--- DataFrame Carros Alemães ---")
print(df_german)

print("\n--- DataFrame Carros Japoneses ---")
print(df_japanese)

# 3. Concatenar os dois DataFrames
# Nota: Padronizamos os nomes das colunas para minúsculas antes de concatenar,
# garantindo que as colunas 'Company' e 'company' fiquem unificadas.
df_german.columns = df_german.columns.str.lower()
df_japanese.columns = df_japanese.columns.str.lower()

df_carros_total = pd.concat([df_german, df_japanese], ignore_index=True)

print("\n--- DataFrames Concatenados ---")
print(df_carros_total)