from typing import Any
import requests
from dotenv import load_dotenv
import os

def get_news_headers(year, month):

    load_dotenv()  # load environment variables from .env

    # Constants
    NY_TIMES_API_KEY = os.environ.get("NY_TIMES_API_KEY")

    url = f'https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key={NY_TIMES_API_KEY}'
    r = requests.get(url)
    print('Status code:', r.status_code)

    submission_ids = r.json()
    submission_res = submission_ids['response']

    docs = submission_res['docs']

    main_title = []

    for i in range(5): #fetch only the top 5 headlines of the month
        a = docs[i]
        title = a['headline']
        main_title.append(title['main'])

    text = "/n ".join(a for a in main_title)
    return text

def main():
    year = 2023
    month = 10
    news_headers = get_news_headers(year, month)
    print(news_headers)

if __name__ == "__main__":
    main()