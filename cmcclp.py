from math import isqrt, trunc
from os import read, write
from typing import Generator, Mapping
from pandas.core.construction import array
from pandas.core.frame import DataFrame
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import csv
import pandas as pd
from sys import argv
import sys
import getopt
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'500',
  'convert':'INR'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '02c65827-46a1-4766-86fc-c9833d6a3462',
}
session = Session()
session.headers.update(headers)
def file():
    csv_file = None
    excel_file=None
    argv=sys.argv[1:]
    try:
        opts,args = getopt.getopt(argv,"c:e:",["csv=","excel="])
    except:
        print("Error")
    for opt,csvwriter in opts:
        if opt in['-c','--csv']:
            csv_file= csvwriter
        print(csv_file)
        try:
            with open(argv[1],"w") as csvfile: 
                csvwriter = csv.writer(csvfile)
                response = session.get(url, params=parameters)
                data = json.loads(response.text)
                fieldname = list(data["data"][0].keys())
                csvwriter.writerow(fieldname)
                for value in data["data"]:
                    try:
                        csvwriter.writerow(value.values())
                    except:
                        pass

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)

    for value,Xlwriter in opts:
        if value in ['-e','--excel']:
            excel_file=Xlwriter
        print(excel_file)
        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            df = DataFrame(data["data"])
            Xlwriter=pd.ExcelWriter(argv[1])
            df.to_excel(Xlwriter, index=False)
            Xlwriter.save()
        except:
            pass

file()
