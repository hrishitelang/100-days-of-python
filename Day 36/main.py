import os
import requests
from newsapi import NewsApiClient
from twilio.rest import Client
from dotenv import load_dotenv

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

'''
Note that even though I've written email_port as an integer and DEBUG as a boolean, when they are read into your project 
they are interpreted as strings, so they will still need to be converted! Conclusion: environment variables are always strings.

If you're worried about the security of the text file on your PC, then you could encrypt the file using something like AXCrypt.
'''
load_dotenv("C:/Users/Admin/Desktop/100 Days of Python/Day 36/.env")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_ID = os.getenv("STOCK_API_ID")
NEWS_API_ID = os.getenv("NEWS_API_ID")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 
parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'outputsize': 'compact',
    'apikey': STOCK_API_ID
}

response = requests.get(STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()
# print(data)
yesterday = float(data['Time Series (Daily)']['2021-02-19']['4. close'])
day_before = float(data['Time Series (Daily)']['2021-02-18']['4. close'])
# print(yesterday)
# print(day_before)
price = (yesterday-day_before)/day_before * 100
if price < 0:
    abs_price = abs(price)
    # print(abs_price)
if price > 5:
    print('Get news')


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
newsapi = NewsApiClient(api_key=NEWS_API_ID)

all_articles = newsapi.get_everything(q=COMPANY_NAME,
                                      from_param='2021-02-20',
                                      to='2021-02-21',
                                      language='en')
first_three_articles = all_articles["articles"][1:4]
# print(first_three_articles[0]['title'])
# print(first_three_articles[0]['description'])


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
client = Client(account_sid, auth_token)

if price < 0:
    sensex = f"🔻{abs_price:.2f}%"
else:
    sensex = f"🔺{abs_price:.2f}%"
for i in range(3):
    message = client.messages \
                    .create(
                         body=f"TSLA: {sensex}\nHeadline: {first_three_articles[i]['title']}\nBrief: {first_three_articles[i]['description']}",
                         from_='+12107750561',
                         to='+918879561392'
                     )

    print(message.status)


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

