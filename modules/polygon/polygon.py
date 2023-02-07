import requests
import os
import json
import copy
import pandas as pd

polygon_key = os.environ.get("POLYGON_KEY")

# Date in YYYY-MM-DD format
open_close = "https://api.polygon.io/v1/open-close/{ticker}/{date}?adjusted=true&apiKey={polygon_key}"
company_details = "https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={polygon_key}"

def get_stock_data(ticker):
 r = requests.get(company_details.format(polygon_key=polygon_key, ticker=ticker))
 response_text = r.text
 response_dict = json.loads(response_text)
 results_dict = response_dict["results"]
 interested_keys = ["ticker", "name", "homepage_url","phone_number", "address", "total_employees",  "market_cap", "currency_name"]
 compressed_dict = {}
 for key in interested_keys:
  if key == "address":
   address_string = ""
   for a_key in results_dict["address"].keys():
    address_string = address_string + " " + results_dict["address"][a_key]
   compressed_dict[key] = address_string
  else:
   compressed_dict[key] = results_dict[key]
 return copy.deepcopy(compressed_dict)


tickers = ["AAPL", "AMZN", "TSLA", "GOOGL"]
ticker_data = []
for ticker in tickers:
 ticker_data.append(get_stock_data(ticker))