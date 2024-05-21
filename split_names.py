import pandas as pd

# SEPARAR COLUNAS POR DELIMITADOR
df = pd.read_csv("SPLIT.csv", encoding='latin1')
df[["NOME1","NOME2","NOME3"]] = df["NOME"].str.split(" ", expand=True, n=2)
df.to_csv("SPLITok.csv", index=False)


# SEPARAR COLUNAS POR DELIMITADOR "/"
'''df = pd.read_csv("SPLIT.csv")
df[["COLO","DATA COLONO"]] = df["Status"].str.split("/", expand=True, n=2)
df.to_csv("SLIPTok.csv", index=False)'''
