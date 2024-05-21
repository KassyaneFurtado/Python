import pandas as pd 

# IDENTIFICAR DADOS DUPLICADOS
df = pd.read_csv("CASOSGBM.csv")
de = df.drop_duplicates
print(df)
