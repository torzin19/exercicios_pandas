import pandas as pd

# 1. Definir os dois dicionários com os dados
Car_price = {
    'Company': ['Toyota', 'Honda', 'Bmv', 'Audi'],
    'Price': [23845, 17995, 135925, 71400]
}

Car_horsepower = {
    'Company': ['Toyota', 'Honda', 'Bmv', 'Audi'],
    'horsepower': [141, 80, 182, 160]
}

# 2. Criar os dois DataFrames
car_Price_Df = pd.DataFrame(Car_price)
cars_Horsepower_Df = pd.DataFrame(Car_horsepower)

# 3. Mesclar (merge) os dois DataFrames usando a coluna 'Company' como chave
cars_df = pd.merge(car_Price_Df, cars_Horsepower_Df, on='Company')

# 4. Exibir o resultado final
print("--- DataFrame Final Mesclado ---")
print(cars_df)