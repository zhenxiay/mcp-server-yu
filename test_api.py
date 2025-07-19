from typing import Any
import requests
from dotenv import load_dotenv
import os

load_dotenv()  # load environment variables from .env

# Constants

NY_TIMES_API_KEY = os.environ.get("NY_TIMES_API_KEY")
USER_AGENT = "weather-app/1.0"

def get_news_headers(year, month):
    url = f'https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key={NY_TIMES_API_KEY}'
    r = requests.get(url)
    print('Status code:', r.status_code)

    submission_ids = r.json()
    submission_res = submission_ids['response']

    docs = submission_res['docs']

    main_title = []

    for i in range(5):
        a = docs[i]
        title = a['headline']
        main_title.append(title['main'])

    text = " ".join(a for a in main_title)
    return text

if __name__ == "__main__":
    text = get_news_headers(2024, 10)
    print(text)