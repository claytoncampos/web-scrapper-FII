import pandas as pd
import time
from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


inicio = time.time()

# DISABLE VISIBLE WEB BROWSER
options = Options()
options.add_argument("--headless")
print ("Headless Firefox Initialized")

#VARIABLE TO SCRAPPER
BTN_POPUP = '//*[@id="popup-close-button"]'
BTN_SELECT_COLS = '//*[@id="colunas-ranking__select-button"]'
BTN_SELECT_ALL_COLS = '/html/body/div[6]/div[1]/div/div[2]/div[2]/ul/li[1]/label/span'
COLUMN = '/html/body/div[6]/div[2]/div/div/div/table/thead/tr/th' #30
ROW = '/html/body/div[6]/div[2]/div/div/div/table/tbody/tr' #430

#BTN_POPUP,BTN_SELECT_COLS,BTN_SELECT_ALL_COLS,COLUMN,ROW
#GET FIIS
def get_fiis():
    url = "https://www.fundsexplorer.com.br/ranking"
    browser = webdriver.Firefox(options=options)
    browser.get(url)

#    time.sleep(2)
    browser.find_element(By.XPATH,BTN_POPUP).click()
#    time.sleep(1)
    browser.find_element(By.XPATH,BTN_SELECT_COLS).click()
#    time.sleep(1)
    browser.find_element(By.XPATH,BTN_SELECT_ALL_COLS).click()
#    time.sleep(1)
    N_COLS = len(browser.find_elements(By.XPATH,COLUMN))
#    time.sleep(1)
    N_ROWS = len(browser.find_elements(By.XPATH,ROW))

    fiiDF =[]
    list_fii_DF =[]
    columns =[]

    #GET VALUE HEADER TABLE
    for i in range(1,N_COLS+1):
        value_col = browser.find_element(By.XPATH, f'{COLUMN}[{i}]').text
        columns.append(value_col)
        print(columns)

    #GET VALUES ROWS TABLE
    for r in range(1, N_ROWS+1): #N_ROWS+1 (LEMBRAR DE MUDAR PAR PEGAR TODAS LINHAS)
        for c in range(1, N_COLS+1):
            # obtaining the text from each column of the table
            value = browser.find_element(By.XPATH, f"{ROW}["+str(r)+"]/td["+str(c)+"]").text
            print(value)
            fiiDF.append(value)
        list_fii_DF.append(fiiDF[:])
        fiiDF.clear()

    browser.close()
    browser.quit()

    return list_fii_DF, columns

#VARIABLES TO ARCHIVE
path_extract ="C:/web-scrapper-FII/data/raw"
dataset_name ="planilha_geral_fii2"
file_name = f"{path_extract}/{dataset_name}.xlsx"

#RUN SCRAPPER
data = get_fiis()
df = data[0]
columns = data[1]
df = pd.DataFrame(df,columns=columns)

#CREATE ARCHIVE XLSX
df.to_excel(file_name, index=False)
print(f'{file_name} criada com sucesso!!')


fim = time.time()
print(f'tempo total: {(fim - inicio) // 60}')