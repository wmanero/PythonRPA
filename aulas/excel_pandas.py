import pandas as pd

df = pd.read_excel('tabela_clientes.xlsx')

print("Quantidade de linha e colunas")
print(df.shape)
print("Nomes das colunas")
print(df.columns)
print("Mostra 5 primeiras linhas ou de acordo com valor informado")
print(df.head())
print("Mostra últimas 5 linhas ou de acordo com valor informado.")
print(df.tail())

print("Recebe o valor na variável.")
cpf = df.values[0,0]
print(cpf)
print("Mostra todos os dados do index informado.")
print(df.iloc[0])