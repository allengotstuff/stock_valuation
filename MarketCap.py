import requests
import matplotlib.pyplot as plt
from math import log
import datetime
import matplotlib.dates as mdates

from Utility import RevUtility
import plotly.graph_objs as go
import plotly.plotly as py
from FinDataApi import MarcoTrendsApi




def main():
    STOCK_SYB = "NTES"
    COMPANY = "netease"
    INFO_TYPE = "revenue"


    cap_info = MarcoTrendsApi().fetchMarketCapInfo(STOCK_SYB)

    # read market cap data from api
    x_val = [x for x in cap_info[0]]
    y_val = [x * 1000 for x in cap_info[1]]## in million usd

    utilityTool = RevUtility()

    revenueList = MarcoTrendsApi().fetchFinancialInfo(STOCK_SYB,COMPANY,INFO_TYPE)

    paybackTime = []


    for i in range(len(x_val)):
        cap = y_val[i]

        current_date = x_val[i]

        revenue = utilityTool.findRevenueForGiveDate(current_date, revenueList)[1]

        if revenue != None and revenue != 0:
            paybackRatio = cap/float(revenue)
            paybackTime.append(paybackRatio)
        else:
            paybackTime.append(0)

    data = [go.Scatter(x=x_val, y=paybackTime)]
    py.plot(data, filename = COMPANY)







if __name__ == "__main__":
    main()
