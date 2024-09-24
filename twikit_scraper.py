from twikit import Client
import os

USERNAME = os.getenv("TWITTER_USERNAME")
EMAIL = os.getenv("TWITTER_EMAIL")
PASSWORD = os.getenv("TWITTER_PASSWORD")

# Initialize client
client = Client('en-US')

async def main():
    await client.login(
        auth_info_1=USERNAME,
        auth_info_2=EMAIL,
        password=PASSWORD
    )

    tweets = await client.search_tweet('vacina hpv', 'Latest')

    for tweet in tweets:
        print(tweet.user.name, tweet.text, tweet.created_at)

if __name__ == "__main__":
    asyncio.run(main())
