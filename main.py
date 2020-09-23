import requests
import xml.etree.ElementTree as ET
from datetime import date

store = "c5mefzzzyn"
client = "lpjzv661peha9q6b91aonft10ak0yu3"
token = "3mg9v0fajbdoi0lf7kqb3c9k36a81zw"

today = date.today()
day = today.strftime("%Y-%m-%d")

# orderResponse = requests.get(f"https://api.bigcommerce.com/stores/{store}/v2/orders?min_date_created={day}",
orderResponse = requests.get(f"https://api.bigcommerce.com/stores/{store}/v2/orders?min_date_created=2020-09-17",
                             headers={
                                 "x-auth-client": "lpjzv661peha9q6b91aonft10ak0yu3",
                                 "x-auth-token": "3mg9v0fajbdoi0lf7kqb3c9k36a81zw"
                             }
                             )

orderRoot = ET.fromstring(orderResponse.content)

for order in orderRoot:

    couponResponse = requests.get(f"https://api.bigcommerce.com/stores/{store}/v2/orders/{order[0].text}/coupons",
                                  headers={
                                      "x-auth-client": "lpjzv661peha9q6b91aonft10ak0yu3",
                                      "x-auth-token": "3mg9v0fajbdoi0lf7kqb3c9k36a81zw"
                                  }
                                  )

    if couponResponse.status_code == 200:
        print(couponResponse.content)

    print(order[0].text, order[3].text, order[48].text)




