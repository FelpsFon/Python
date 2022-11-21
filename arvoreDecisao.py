import pandas as pd

baseDados = "Base-Dados.csv"

df = pd.read_csv(baseDados, index_col=0)

print(df)
print(type(df))

# if df.columns[3] == 1:
#   df.to_csv("dfSaida.csv", index=False)