import requests
from twilio.rest import Client


# API
STOCK_API = "ET1UWGVOUC8NVYBN"
NEWS_API = "80f6068367f2474e8a0e691e555237ea"
ACCOUNT_SID = "ACfb9a6b8aa9e4675b0d2abd5179828bb6"
AUTH_TOKEN = "bc6c1bff35b16f91222411b8793112f9"


# PARAMETERS
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": STOCK_API
}

# STOCK DATA
stock_response = requests.get("https://www.alphavantage.co/query", params=stock_parameters)
stock_response.raise_for_status()

data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
print(data_list)

today_close = data_list[0]["4. close"]
print(today_close)

yesterday_close = data_list[1]["4. close"]
print(yesterday_close)
diff_total = float(today_close) - float(yesterday_close)

emoji = None

if diff_total > 0:
    emoji = '⬆️'
else:
    emoji = '⬇️'

in_percentage = round((diff_total / float(yesterday_close)) * 100)


if abs(in_percentage) > 1:
    # NEWS DATA
    news_parameters = {
        "q": "Tesla",
        "apiKey": NEWS_API
    }

    news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()

    news = news_response.json()["articles"]
    articles = news[:3]

    print(articles)

    # SEND MESSAGE
    formatted_text = [f"TSLA: {emoji}{diff_total}%\nHeadline: {article['title']}\nBrief: {article['description']}" for article in articles]

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    for article in formatted_text:
        client.messages.create(
                             body=article,
                             from_='+16165800849',
                             to='+918971818410'
        )

        print("Sent")
