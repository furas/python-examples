import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

url = "https://scon.stj.jus.br/SCON/legaplic/toc.jsp?materia=%27Lei+8.429%2F1992+%28Lei+DE+IMPROBIDADE+ADMINISTRATIVA%29%27.mat.&b=TEMA&p=true&t=&l=1&i=18&ordem=MAT,@NUM"

option = Options()
option.headless = True
driver = webdriver.Firefox()

driver.get(url)
time.sleep(5)

driver.find_element(by=By.LINK_TEXT, value='§ 6o A ação será instruída com documentos ou justificação que contenham indícios suficientes da existência do ato de improbidade ou com razões fundamentadas da impossibilidade de apresentação de qualquer dessas provas, observada a legislação vigente, inclusive as disposições inscritas nos arts. 16 a 18 do Código de Processo Civil. (Incluído pela Medida Provisória nº 2.225-45, de 2001)').click()

time.sleep(5)

driver.switch_to.window(driver.window_handles[-1]) # Change the focus to the new page, otherwise I can not scrap its content

element = driver.find_element(by=By.CLASS_NAME, value="listadocumentos")
html_content = element.get_attribute('outerHTML')

# --- before all pages --

header = []
content = []

# --- loop ---

for n in range(5):
    print('--- page:', n+1, '---')
    # --- get data from page --
    
    resultados = BeautifulSoup(driver.page_source, 'lxml')
    paragrafoBRS = resultados.find_all('div', attrs={'class':'paragrafoBRS'})
    
    for each in paragrafoBRS:
        header.append(each.find('div', {'class':'docTitulo'}).text)
        content.append(each.find(['div','pre'], {'class':'docTexto'}).text)
    
    print('len(content):', len(content))
    
    # --- load next page ---
    
    print('click')
    driver.find_element(by=By.CLASS_NAME, value='iconeProximaPagina.temHint').click()
    
    time.sleep(5)

# --- after loop ---

driver.quit()

dataDict = {}
df = pd.DataFrame()

for i in range(len(header)):
    if header[i] in dataDict:
        df = df.append(pd.DataFrame(dataDict), ignore_index=True)
        dataDict = {}

    dataDict[header[i]] = [content[i]]

df.to_excel('data.xlsx')

