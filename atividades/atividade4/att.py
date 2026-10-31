import pandas as pd

# PRIMEIRA PARTE
df_supermercado = pd.read_csv("estoque_supermercado.csv",
                              sep=",",
                              dtype={"preco": str,
                                     "quantidade": str})

# SEGUNTA PARTE
df_supermercado["precos_limpos"] = (df_supermercado["preco"]
                                    .str.replace(r'[^\d,.\-]', '', regex=True))
df_supermercado["precos_limpos"] = pd.to_numeric(df_supermercado["precos_limpos"])
preco_medio = df_supermercado["precos_limpos"].mean()
df_supermercado["precos_limpos"] = (df_supermercado["precos_limpos"]
                                    .fillna(preco_medio).round(2))
# sobreescrevendo a coluna preço pela coluna limpa com dados float
df_supermercado["preco"] = df_supermercado["precos_limpos"]
#  retiro a coluna usada na analise
df_supermercado = df_supermercado.drop(columns=["precos_limpos"])
# print(df_supermercado["preco"])

# TERCEIRA PARTE
df_supermercado["quantidade"] = (
    df_supermercado["quantidade"].str.replace(r"\D", "", regex=True)
)
df_supermercado["quantidade"] = pd.to_numeric(df_supermercado["quantidade"])
df_supermercado["quantidade"] = df_supermercado["quantidade"].fillna(0)
df_supermercado["quantidade"] = df_supermercado["quantidade"].astype(int)

# QUARTA PARTE
df_supermercado["setor"] = (
    df_supermercado["setor"].str.strip().str.lower()
)

df_supermercado["setor"] = df_supermercado["setor"].fillna("sem setor")
# print(df_supermercado["setor"])

# QUINTA PARTE
df_supermercado["data_vencimento"] = df_supermercado["data_vencimento"].fillna("30/10/2027")
df_supermercado["data_vencimento"] = pd.to_datetime(
    df_supermercado["data_vencimento"],
    dayfirst=True,
)

data_vencimento = df_supermercado[
    df_supermercado["data_vencimento"] < "01-01-2027"
]
print(data_vencimento)
# SEXTA PARTE -> A TERMINAR
# print(df_supermercado.to_string())





