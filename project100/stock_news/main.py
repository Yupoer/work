import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY_STOCK = "CXOSSLAFA7J2T3DW"
API_KEY_NEWS = "0dcfd92ecb754ad3b9ef5ad88f306a78"
account_sid = "AC4c58bbfb1758b33f1af719b6c93e6983"
auth_token = "59641c6f5969156df94aab23ef5a0532"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY_STOCK
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in stock_data.items()]
yesterday_data = data_list[0]
yesterday_close_price = yesterday_data["4. close"]
day_before_yesterday_data = data_list[1]
day_before_yesterday_close_price = day_before_yesterday_data["4. close"]

difference = abs(float(yesterday_close_price) - float(day_before_yesterday_close_price))
diff_percent = round((difference / float(yesterday_close_price)) * 100)
up_down = None
if difference > 0:
    up_down = "⬆"
else:
    up_down = "⬇"

if abs(diff_percent) > 0.7:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": API_KEY_NEWS
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]

    formatted_article = [f"{STOCK_NAME}:{up_down}{diff_percent}%\nHeadline: {article['title']}.\n{article['description']}" for article in three_articles]

    client = Client(account_sid, auth_token)
    for article in formatted_article:
        message = client.messages \
            .create(
            body=article,
            from_="+14436029249",
            to="+886905734830"
        )

