import os
from sqlalchemy import create_engine
import pandas as pd


sql_endpoint = os.environ.get("SQL_ENDPOINT")
sql_pw = os.environ.get("SQL_PW")
sql_user = os.environ.get("SQL_USER")
sql_db = os.environ.get("SQL_DB")


def get_sql_engine():
    engine = create_engine(f'postgresql+psycopg2://{sql_user}:{sql_pw}@{sql_endpoint}/{sql_db}')
    return engine


def run_query(query):
    engine = get_sql_engine()
    conn = engine.connect()
    result = conn.execute(query)
    return result


def get_connection():
    engine = get_sql_engine()
    return engine.connect()


def convert_q_to_df(query):
    result = run_query(query)
    df = pd.DataFrame(result.fetchall())
    df.columns = result.keys()
    return df


def fetch_first_result(query):
    result = run_query(query)
    return result.fetchone()[0]


def convert_q_to_list(query):
    result = run_query(query)
    l = []
    for row in result:
        l.append(row[0])
    return l