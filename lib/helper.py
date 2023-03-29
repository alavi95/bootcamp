import os
import sys
sys.path.append(os.path.realpath(__file__).split("bootcamp")[0]+"bootcamp")

from lib.env import *
from datetime import datetime, timedelta


def get_yesterday_date():
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    return yesterday.strftime("%Y-%m-%d")