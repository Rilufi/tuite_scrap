from twikit import Client
import os
import asyncio

USERNAME = os.getenv("TWITTER_USERNAME")
EMAIL = os.getenv("TWITTER_EMAIL")
PASSWORD = os.getenv("TWITTER_PASSWORD")

async def main():
    await client.login(
        username=USERNAME,
        password=PASSWORD
    )

asyncio.run(main())
# Initialize client
client = Client('en-US')

