from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Configurações do Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")  # Rodar em segundo plano (sem abrir a interface gráfica)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=chrome_options)

# URL de busca no Twitter/X
url = 'https://twitter.com/search?q=vacina%20HPV%20OR%20vacina%20de%20HPV&src=typed_query&f=live'

# Acessar a página
driver.get(url)
time.sleep(5)  # Espera a página carregar

# Extrair tweets
tweets = driver.find_elements_by_css_selector("article")

for tweet in tweets:
    print(tweet.text)

driver.quit()
