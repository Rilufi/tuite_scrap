from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os

# Configuração do WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
wait = WebDriverWait(driver, 10)

# Função para fazer login
def login(username, password):
    driver.get("https://twitter.com/login")
    sleep(3)

    # Localizar o campo de login
    email_input = wait.until(EC.presence_of_element_located((By.NAME, "text")))
    email_input.send_keys(username)
    email_input.send_keys(Keys.RETURN)
    
    # Esperar e inserir a senha
    sleep(2)
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    
    sleep(5)  # Esperar o redirecionamento após o login

# Insira aqui suas credenciais
username = os.getenv("TWITTER_USERNAME")
password = os.getenv("TWITTER_PASSWORD")

# Chamar a função de login
login(username, password)

# Verificar se o login foi bem-sucedido
if "login" not in driver.current_url:
    print("Login realizado com sucesso!")
else:
    print("Erro no login.")

driver.quit()
