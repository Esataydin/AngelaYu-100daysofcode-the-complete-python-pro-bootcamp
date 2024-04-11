from newsapi import NewsApiClient
from twilio.rest import Client

import requests
from datetime import date


STOCK: str = "TSLA"
COMPANY_NAME: str = "Tesla Inc"

api_key_stock: str = YOUR_STOCK_API_KEY
api_key_news: str = YOUR_NEWS_API_KEY

account_sid: str = YOUR_TWILIO_ACCOUNT_SID
auth_token: str = YOUR_TWILIO_AUTH_TOKEN

i: int = 0
close_last_days: list[float] = []
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={api_key_stock}'
r = requests.get(url)
data = r.json()
days_data = data["Time Series (Daily)"]
for daily_data in days_data:
    if i == 2:
        break
    i += 1
    close_last_days.append(days_data[daily_data]["4. close"])

difference = float(close_last_days[0]) - float(close_last_days[1])

today = date.today()

month = today.month
year = today.year
day = today.day

newsapi = NewsApiClient(api_key=YOUR_NEWS_API_KEY)

all_articles = newsapi.get_everything(q="tesla",
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com,engadget.com',
                                      from_param=f'{year}-11-{day}',
                                      to=f'{year}-{month}-{day}',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
articles = []
for article in all_articles["articles"]:
    title = article["title"]
    description = article["description"]
    news = str(title) + "\n" + str(description) + "\n"
    articles.append(news)

# Sends a separate message with the percentage change and each article's title and description to your phone number.
difference_percentage = round(difference*100/float(close_last_days[0]))
message = ""
for news_ in articles:
    message = message + str(news_)
i = 0

for _ in articles:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body=f"{STOCK}: {difference_percentage}\n{articles[i]}",
            from_="[TWILIO_NUMBER]",
            to="[TO_NUMBER]"
        )
    i += 1

    print(message.sid)



