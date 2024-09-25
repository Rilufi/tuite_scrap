import snscrape.modules.twitter as sntwitter
import csv

query = 'vacina hpv lang:pt since:2024-09-25 until:2024-09-26'

# Create a CSV file to store the tweets
with open('tweets.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Tweet_count', 'Username', 'Text', 'Created At', 'Retweets', 'Likes'])

    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i > 10:  # Adjust this limit according to your needs
            break
        writer.writerow([i+1, tweet.user.username, tweet.content, tweet.date, tweet.retweetCount, tweet.likeCount])

print(f'Done! Collected {i+1} tweets.')
