import datetime
import os
import pathlib

DATE_START = str(datetime.datetime.today().date() - datetime.timedelta(days=1))
DATA_PATH = pathlib.Path("data/")
DATA_PATH.mkdir(parents=True, exist_ok=True)

HASHTAG = 'depression'
JSON_FILENAME = DATA_PATH / f"{datetime.datetime.today().date()}.json"

def sns_scrape():
    command = (
        f'snscrape --jsonl --progress --since {DATE_START} '
        f'twitter-hashtag "{HASHTAG}" > "{JSON_FILENAME}"'
    )
    os.system(command)

if __name__ == "__main__":
    sns_scrape()
