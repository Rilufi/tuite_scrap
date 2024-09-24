import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Definir a URL da busca no Twitter
query_url = 'https://twitter.com/search?q=vacina%20HPV%20OR%20vacina%20de%20HPV&src=typed_query&f=live'

# Configuração do WebDriver para Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Inicializar o driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 10)

# Função para buscar e coletar os tweets
def scrape_tweets():
    print("Acessando a URL...")
    driver.get(query_url)
    sleep(5)

    # Salvar o código-fonte da página para inspeção
    with open("page_source.html", "w") as f:
        f.write(driver.page_source)
    
    tweets = []
    
    # Forçar scroll progressivo até carregar todos os tweets
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        elements = driver.find_elements(By.XPATH, '//article[@role="article"]//div[@lang]')
        print(f"Encontrados {len(elements)} elementos na iteração.")
        
        if elements:
            for el in elements:
                tweets.append(el.text)
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    
    return tweets

# Realizar scraping
tweets = scrape_tweets()

# Salvar os resultados em um arquivo
with open('tweets_hp_vacina.csv', 'w') as file:
    for tweet in tweets:
        file.write(f"{tweet}\n")

# Fechar o driver
driver.quit()

print(f"Coletados {len(tweets)} tweets.")
