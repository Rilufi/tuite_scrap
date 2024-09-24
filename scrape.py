import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Definir a URL da postagem de interesse ou busca no Twitter
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

# Função de login (caso seja necessário)
def login():
    driver.get('https://x.com/i/flow/login')
    email_input = wait.until(EC.presence_of_element_located((By.NAME, "text")))
    email_input.send_keys(os.getenv("TWITTER_EMAIL"))
    
    next_btn = driver.find_element(By.CSS_SELECTOR, 'button span span')
    next_btn.click()
    sleep(3)

    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password_input.send_keys(os.getenv("TWITTER_PASSWORD"))

    login_btn = driver.find_element(By.CSS_SELECTOR, 'button span span')
    login_btn.click()
    sleep(5)

# Função para buscar e coletar os comentários
def scrape_tweets():
    driver.get(query_url)
    sleep(3)
    
    tweets = []
    
    for _ in range(5):  # Loop para rolar a página e carregar mais tweets
        elements = driver.find_elements(By.XPATH, '//div[@data-testid="tweetText"]')
        for el in elements:
            tweets.append(el.text)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)  # Aguardar enquanto a página carrega
    
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
