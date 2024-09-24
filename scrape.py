import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, UnexpectedAlertPresentException, NoAlertPresentException
from time import sleep
from selenium.webdriver.common.keys import Keys

chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
wait = WebDriverWait(self.driver, 15)

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
