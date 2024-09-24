import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import datetime

# Definir a query de busca
query = "(vacina HPV OR vacina de HPV) since:2023-01-01 until:2023-12-31"

# Limitar o número de tweets a serem coletados
max_tweets = 100

# Lista para armazenar os dados
tweets_list = []

# Scraping
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if i >= max_tweets:
        break
    tweets_list.append([tweet.date, tweet.user.username, tweet.content])

# Criar um DataFrame a partir da lista de tweets
tweets_df = pd.DataFrame(tweets_list, columns=['Date', 'Username', 'Tweet'])

# Salvar o resultado em um arquivo CSV
current_time = datetime.now().strftime("%Y%m%d%H%M%S")
tweets_df.to_csv(f'tweets_hp_vacina_{current_time}.csv', index=False)

print(f"Scraping concluído. {len(tweets_df)} tweets coletados.")
