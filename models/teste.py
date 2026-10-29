import pandas as pd

meus_dados = [
    {
        'nome': 'João',
        'idade': 31,
        'profissao': "Instrutor"
    }
]

df = pd.DataFrame(meus_dados)
print(df)
