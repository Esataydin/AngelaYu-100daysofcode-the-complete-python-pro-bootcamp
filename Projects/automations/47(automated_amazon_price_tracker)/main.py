from twilio.rest import Client
from bs4 import BeautifulSoup

import requests


account_sid = YOUR_TWILIO_ACCOUNT_SID
auth_token = YOUR_TWILIO_AUTH_TOKEN

# it's for example, it can be changed to any product in Amazon.
product_link = "https://www.amazon.com/BELLA-Pre-Heat-Removeable-Dishwasher-Crisping/dp/B08P2PPD6W/ref=sr_1_ \
                        5?crid=2HDG5QUCSVDU1&keywords=air+fryer&nav_sdd=aps&qid=1667641241&qu=eyJxc2MiOiI3LjMxIiwicXNh \
                        IjoiNy4yMiIsInFzcCI6IjYuNzIifQ%3D%3D&refinements=p_n_feature_two_browse-bin%3A17686891011&rni \
                        d=17686890011&s=kitchen&sprefix=air+fryer&sr=1-5"

# Headers for request.get to be used in Amazon properly. Amazon doesn't allow to get site data without proper headers.
headers = {
    "Accept-Language": "en-US",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/92.0.4561.33"
}

response = requests.get(product_link, headers=headers)
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

price_whole = soup.find(name="span", class_="a-price-whole").text
price_fraction = soup.find(name="span", class_="a-price-fraction").text
product_name = soup.find(name="span", id="productTitle").text

full_price = float(f"{price_whole}{price_fraction}")

if full_price < 45:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"{product_name}is only:\n{full_price}",
        from_=YOUR_TWILIO_NUMBER,
        to=YOUR_NUMBER
    )