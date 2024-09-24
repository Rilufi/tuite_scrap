from twikit import Client
import os
import asyncio

USERNAME = os.getenv("TWITTER_USERNAME")
EMAIL = os.getenv("TWITTER_EMAIL")
PASSWORD = os.getenv("TWITTER_PASSWORD")

async def main():
    client = Client('en-US')
    await client.login(
        auth_info_1e=USERNAME,
        password=PASSWORD
    )

asyncio.run(main())
# Initialize client


