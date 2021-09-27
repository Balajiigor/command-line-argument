from math import isqrt
from os import read, write, writev
from typing import Generator
from pandas.core.frame import DataFrame
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import sys
import getopt
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '02c65827-46a1-4766-86fc-c9833d6a3462',
}

session = Session()
session.headers.update(headers)
def file():
    excel_file = None
    argv = sys.argv[1:]
    try:
        opts,args = getopt.getopt(argv,'e:',["excel="])

    except:
        pass
    for opt,writer in opts:
        if opt in ['-e','--excel']:
            excel_file = writer
            print(excel_file)
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        data = write('jos.json')
        df = DataFrame(data["data"])
        writer=pd.ExcelWriter(argv[1])
        df.to_excel(writer, index=False)
        writer.save()
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
    maindata = pd.read_excel(argv[1])
    maindata.drop(columns=["quote"],index=1,inplace=True)
    maindata.to_excel(argv[1])
file()