import requests
from twilio.rest import Client


# API
STOCK_API = "ET1UWGVOUC8NVYBN"
NEWS_API = "80f6068367f2474e8a0e691e555237ea"
ACCOUNT_SID = "ACfb9a6b8aa9e4675b0d2abd5179828bb6"
AUTH_TOKEN = "bc6c1bff35b16f91222411b8793112f9"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": STOCK_API
}


news_parameters = {
    "q": "Tesla",
    "from": "2022-01-24",
    "sortBy": "popularity",
    "apiKey": NEWS_API
}


stock_response = requests.get("https://www.alphavantage.co/query", params=stock_parameters)
stock_response.raise_for_status()

data = stock_response.json()["Time Series (Daily)"]
today_close = data["2022-01-21"]["4. close"]
print(today_close)

yesterday_close = data["2022-01-20"]["4. close"]
print(yesterday_close)
diff_total = float(today_close) - float(yesterday_close)
print(diff_total)

in_percentage = -5.26
mess = ""
if in_percentage > 0:
    mess = f"TSLA up over {in_percentage}"
else:
    mess = f"TSLA down over {in_percentage}"

print(mess)


news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
news_response.raise_for_status()

news_data = news_response.json()["articles"][0]

headline = news_data["title"]
print(headline)

brief = news_data["description"]
print(brief)


send_message = f"{mess}\nHeadline: {headline}\nBrief: {brief}"
print(send_message)

client = Client(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
                     body=send_message,
                     from_='+16165800849',
                     to='+918971818410'
)

print("Sent")
