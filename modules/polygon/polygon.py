import os
import sys
sys.path.append(os.path.realpath(__file__).split("bootcamp")[0]+"bootcamp")

from lib.helper import *
import requests
import os
import json
import copy
import pandas as pd


def get_stock_data(ticker):
    company_details = "https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={polygon_key}"
    r = requests.get(company_details.format(polygon_key=polygon_key, ticker=ticker))
    response_text = r.text
    response_dict = json.loads(response_text)
    results_dict = response_dict["results"]
    interested_keys = ["ticker", "name", "homepage_url","phone_number", "address", "total_employees",  "market_cap", "currency_name"]
    compressed_dict = {}
    for key in interested_keys:
        try:
            if key == "address":
                address_string = ""
                for a_key in results_dict["address"].keys():
                    address_string = address_string + " " + results_dict["address"][a_key]
                compressed_dict[key] = address_string
            else:
                compressed_dict[key] = results_dict[key]
        except:
            continue
    return copy.deepcopy(compressed_dict)


def get_price_data(ticker, date):
    open_close = "https://api.polygon.io/v1/open-close/{ticker}/{date}?adjusted=true&apiKey={polygon_key}"
    r = requests.get(open_close.format(polygon_key=polygon_key, ticker=ticker, date=date))
    response_text = r.text
    response_dict = json.loads(response_text)
    interested_keys = ["from", "symbol", "open", "high", "low", "close"]
    compressed_dict = {}
    for key in interested_keys:
        try:
            compressed_dict[key] = response_dict[key]
        except:
            continue
    return copy.deepcopy(compressed_dict)


# Pass through a list of tickers
def get_company_data_df(tickers):
    ticker_data = []
    for ticker in tickers:
        try:
            r = get_stock_data(ticker.upper())
            r["status"] = "success"
            ticker_data.append(copy.deepcopy(r))
        except:
            ticker_data.append({"ticker" : ticker, "status" : "failed"})
    return pd.DataFrame(ticker_data)


# Pass through a list of tickers, and a date hardcoded in a string using the YYYY-MM-DD format
def get_stock_data_day_df(tickers, date):
    ticker_prices = []
    for ticker in tickers:
        ticker_prices.append(get_price_data(ticker.upper(), date))
    return pd.DataFrame(ticker_prices)


# Pass through a single ticker as a string and a list of hardcoded dates in a list (using the YYYY-MM-DD format)
def get_stock_history_df(ticker, dates):
    ticker_prices = []
    for date in dates:
        ticker_prices.append(get_price_data(ticker.upper(), date))
    return pd.DataFrame(ticker_prices)


# Sample lists/variables for you to use
ticker = "AMZN"
tickers = ["AMZN", "GOOGL", "AAPL", "TSLA"]
date = "2023-02-06"
dates = ["2023-02-06", "2023-02-01", "2023-01-17", "2023-01-12"]
