from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Inicializando o driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Acesse a página de login do Facebook
driver.get("https://www.instagram.com/accounts/login/")

# Espera a página carregar
time.sleep(3)

# Encontrando os campos de entrada e enviando informações
email_input = driver.find_element(By.ID, "email")
password_input = driver.find_element(By.ID, "pass")

email_input.send_keys("seu_email@example.com")  # Coloque seu email aqui
password_input.send_keys("sua_senha")  # Coloque sua senha aqui

# Encontrando o botão de login e clicando
login_button = driver.find_element(By.NAME, "login")
login_button.click()

# Espera para ver o resultado
time.sleep(5)

# Fechando o navegador
driver.quit()

