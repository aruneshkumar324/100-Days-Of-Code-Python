import requests

response = requests.get("https://api.coinlore.net/api/tickers/")
response.raise_for_status()


data = response.json()["data"]

for x in data:
    # print(x)
    print(x["rank"])

print(len(data))
