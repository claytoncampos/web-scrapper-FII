import pandas as pd
import time
from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# DISABLE VISIBLE WEB BROWSER
options = Options()
options.add_argument("--headless")
print ("Headless Firefox Initialized")

#GET FIIS
url = "https://www.fundsexplorer.com.br/ranking"
browser = webdriver.Firefox(options=options)
browser.get(url)

#SELECT FIELDS
BTN_POPUP = '//*[@id="popup-close-button"]'
BTN_SELECT_COLS = '//*[@id="colunas-ranking__select-button"]'
BTN_SELECT_ALL_COLS = '/html/body/div[6]/div[1]/div/div[2]/div[2]/ul/li[1]/label/span'
COLUMN = '/html/body/div[6]/div[2]/div/div/div/table/thead/tr/th' #30
ROW = '/html/body/div[6]/div[2]/div/div/div/table/tbody/tr' #430

#GET FIELDS
time.sleep(2)
browser.find_element(By.XPATH,BTN_POPUP).click()
time.sleep(1)
browser.find_element(By.XPATH,BTN_SELECT_COLS).click()
time.sleep(1)
browser.find_element(By.XPATH,BTN_SELECT_ALL_COLS).click()
time.sleep(1)
print(len(browser.find_elements(By.XPATH,COLUMN)))
N_COLS = len(browser.find_elements(By.XPATH,COLUMN))
time.sleep(1)
print(len(browser.find_elements(By.XPATH,ROW)))
N_ROWS = len(browser.find_elements(By.XPATH,ROW))

fiiDF =[]
list_fii_DF =[]
columns =[]

#GET VALUE HEADER TABLE
for i in range(1,N_COLS+1):
    value_col = browser.find_element(By.XPATH, f'{COLUMN}[{i}]').text
    columns.append(value_col)

#GET VALUES ROWS TABLE
for r in range(1, 2+1): #N_ROWS+1 (LEMBRAR DE MUDAR PAR PEGAR TODAS LINHAS)
    for c in range(1, N_COLS+1):
        # obtaining the text from each column of the table
        value = browser.find_element(By.XPATH, f"{ROW}["+str(r)+"]/td["+str(c)+"]").text
        fiiDF.append(value)
    list_fii_DF.append(fiiDF[:])
    fiiDF.clear()


extract_path ="C:/web-scrapper-FII/data/raw"
dataset_name ="planilha_geral_fii"
file_name = f"{extract_path}/{dataset_name}.xlsx"
print(file_name)


df = pd.DataFrame(list_fii_DF, columns=columns)
df.to_excel(file_name, index=False)
print(f'{file_name} criada com sucesso!!')
browser.quit()