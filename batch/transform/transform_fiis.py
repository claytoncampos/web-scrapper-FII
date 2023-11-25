import datetime
import pandas as pd


#carrgar DF
df = pd.read_excel("C:/web-scrapper-FII/data/raw/0_planilha_geral_fii.xlsx")
#print(df)

#dropar colunas desnecessarias
df.drop(columns=['DIVIDEND YIELD','DY (3M) ACUMULADO','DY (6M) ACUMULADO', 'DY (3M) MÉDIA','DY (6M) MÉDIA','DY (12M) MÉDIA','DY ANO','RENTAB. PERÍODO'
,'RENTAB. ACUMULADA','VPA','P/VPA','DY PATRIMONIAL','VARIAÇÃO PATRIMONIAL','RENTAB. PATR. PERÍODO','RENTAB. PATR. ACUMULADA','VOLATILIDADE', 'TAX. GESTÃO','TAX. PERFORMANCE','TAX. ADMINISTRAÇÃO'], inplace=True)

#dropar Fundos sem Informações = N/A
print(df)
df = df[df.isna().any(axis=1)]

print(df)

