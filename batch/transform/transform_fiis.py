import datetime
import pandas as pd


#LOAD DATAFRAME
df = pd.read_excel("C:/web-scrapper-FII/data/raw/planilha_geral_fii.xlsx")


#DROPAR COLUNAS DESNECESSÁRIAS
df.drop(columns=['DIVIDEND YIELD','DY (3M) ACUMULADO','DY (6M) ACUMULADO', 'DY (3M) MÉDIA','DY (6M) MÉDIA','DY (12M) MÉDIA','DY ANO','RENTAB. PERÍODO'
,'RENTAB. ACUMULADA','VPA','P/VPA','DY PATRIMONIAL','VARIAÇÃO PATRIMONIAL','RENTAB. PATR. PERÍODO','RENTAB. PATR. ACUMULADA','VOLATILIDADE', 'TAX. GESTÃO','TAX. PERFORMANCE','TAX. ADMINISTRAÇÃO'], inplace=True)

#APLICAR REGRAS DE NEGOCIO
'''
fundos com liquidez acima de 1M ou 800mil
DY  acima de 8%
P/VP menor que 1.2 %
'''
regra_geral = df[(df['LIQUIDEZ DIÁRIA (R$)'] >= '1.000.000,00') & (df['DY (12M) ACUMULADO'] >= "8,00 %") & (df['P/VP'] <= '1.02')]

'''
fundos sem ser de papel qtd ativos acima de 5
sem ser monoinquilino
remover os fundos com cotas acima de R$100
'''
regra_fii_diff_papel = df[(df['SETOR'] != "PAPÉIS") & (df['QUANT. ATIVOS'] > 5)]



print(df.info())


#TOP 10 
#print(regra_geral.head(10))
#print(df.info())

print(df['LIQUIDEZ DIÁRIA (R$)'].astype(float))

