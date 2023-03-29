import os
import sys
sys.path.append(os.path.realpath(__file__).split("bootcamp")[0]+"bootcamp")


from modules.polygon.polygon import *
from modules.sql_connection.sql_connection import *
from lib.helper import *


def get_tickers_from_sql():
    f = open(os.path.realpath(__file__).split("bootcamp")[0]+"bootcamp/projects/polygon_etl/get_tickers.sql", "r")
    query = f.read()
    f.close()
    df = sql_to_df(query)
    tickers = df["ticker"].tolist()
    return tickers



def polygon_etl():
    tickers = get_tickers_from_sql()
    date = get_yesterday_date()
    price_data = []
    success_counter = 0
    for ticker in tickers:
        if success_counter >= 10:
            break
        try:
            d = get_price_data(ticker, date)
            d["ticker"] = ticker
            if "symbol" not in d.keys():
                raise Exception
            else:
                price_data.append(copy.deepcopy(d))
                success_counter = 1
        except:
            continue
    df = pd.DataFrame(price_data)
    df = df.rename(columns={
        "from" : "trading_date"
    })
    del df["symbol"]
    df = df[["ticker", "trading_date", "open", "close", "low", "high"]]
    df_to_sql(df, "pricing_data")
