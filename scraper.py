from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os
import time

# Definindo o caminho do ChromeDriver
chrome_driver_path = r"C:\Users\Wanderson Ferreira\Documents\chromedriver-win64\chromedriver.exe"

# Verificando se o arquivo do ChromeDriver existe
if not os.path.isfile(chrome_driver_path):
    raise FileNotFoundError(f"O ChromeDriver não foi encontrado em: {chrome_driver_path}")

service = Service(chrome_driver_path)

# Inicializando o driver
driver = webdriver.Chrome(service=service)

# Acesse a página de notícias
driver.get("https://news.ycombinator.com/")

# Espera a página carregar
time.sleep(3)

# Coletando títulos das notícias
titles = driver.find_elements(By.CLASS_NAME, 'storylink')

for title in titles:
    print(title.text)

# Fechando o navegador
driver.quit()

