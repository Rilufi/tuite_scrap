import snscrape.modules.twitter as sntwitter
import pandas as pd
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests
from datetime import datetime

# Desativar warnings de SSL
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Defina a query para busca
query = 'vacina HPV'

# Defina o número máximo de tweets que deseja capturar
max_tweets = 100

# Lista para armazenar os resultados
tweets_list = []

# Scraping de tweets
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'{query}').get_items()):
    if i >= max_tweets:
        break
    tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.url])

# Crie um DataFrame com os resultados
tweets_df = pd.DataFrame(tweets_list, columns=['Date', 'Tweet Id', 'Content', 'Username', 'URL'])

# Salve o DataFrame em um arquivo CSV
csv_filename = f"tweets_vacina_hpv_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
tweets_df.to_csv(csv_filename, index=False)

print(f"Scraping concluído. Tweets salvos em {csv_filename}")
