import pandas as pd
import time
from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException

inicio = time.time()

#DISABLE VISIBLE WEB BROWSER
options = Options()
options.add_argument("--headless")
print ("Headless Firefox Initialized")
browser = webdriver.Firefox(options=options)

#VARIABLE TO SCRAPPER
FIELD_TX_ADM = '/html/body/div[3]/main/section/div/div[3]/div/div/div[9]/div[2]/div/span'
FIELD_TX_VACANCIA = '/html/body/div[3]/main/section/div/div[3]/div/div/div[10]/div[2]/div/span'

#VARIABLES TO ARCHIVE
path_load_xlsx = "C:/web-scrapper-FII/data/raw/planilha_geral_fii2.xlsx"
path_extract ="C:/web-scrapper-FII/data/raw"
dataset_name ="planilha_taxas_fii"
file_name = f"{path_extract}/{dataset_name}.xlsx"
columns = [ "FUNDO","TX_ADM","TX_VACANCIA"]

#GET FIIS FROM ARCHIVE XLSX GERAL
def get_list_fii(path_xlsx):
    df = pd.read_excel(path_xlsx)
    return df["FUNDOS"]

#EXTRACT TX FIIS
def get_taxas(fii, FIELD_TX_ADM, FIELD_TX_VACANCIA):
    fundo = []
    taxa_adm =[]
    taxa_vacance =[]
    data =[]
    for fi in fii:
        try:
            url = f"https://investidor10.com.br/fiis/{fi}/"
            print(url)
            
            time.sleep(1)
            browser.get(url)
            
            
            tx_adm = browser.find_element(By.XPATH, f'{FIELD_TX_ADM}').text
            vacancia = browser.find_element(By.XPATH, f'{FIELD_TX_VACANCIA}').text

            fundo.append(fi)
            taxa_adm.append(tx_adm)
            taxa_vacance.append(taxa_vacance)

            data += [[fi] + [tx_adm] + [vacancia]]
        except NoSuchElementException:
            print(f'Fundo {fi} Não localizado no site Investidor10')
            pass
        except TimeoutException:
            print(f'Fundo {fi} Sofreu Timeout do site Investidor10')
            pass

    browser.close()
    browser.quit()


    return data

#RUN SCRAPPER
df_fiis = get_list_fii(path_load_xlsx)
df_taxas_extract = get_taxas(df_fiis,FIELD_TX_ADM,FIELD_TX_VACANCIA)
df_taxas = pd.DataFrame(df_taxas_extract, columns=columns, index=None)

#CREATE ARCHIVE XLSX
df_taxas.to_excel(file_name, index=False)
print(f'{file_name} criada com sucesso!!')


fim = time.time()
print(f'tempo total: {(fim - inicio) // 60} Minutos')

