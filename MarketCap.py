import requests
import matplotlib.pyplot as plt
from math import log
import datetime
import matplotlib.dates as mdates

from Utility import RevUtility
import plotly.graph_objs as go
import plotly.plotly as py
from FinDataApi import MarcoTrendsApi




# api-endpoint
company = "NetEase"
URL = "https://ycharts.com/charts/fund_data.json?securities=include%3Atrue%2Cid%3AFB%2C%2C&calcs=include%3Atrue%2Cid%3Amarket_cap%2C%2C&correlations=&format=real&recessions=false&zoom=5&startDate=&endDate=&chartView=&splitType=single&scaleType=linear&note=&title=&source=false&units=false&quoteLegend=true&partner=&quotes=&legendOnChart=true&securitylistSecurityId=&clientGroupLogoUrl=&displayTicker=false&ychartsLogo=&useEstimates=false&maxPoints=576"
CSV_LOCATION = "/Users/allensun/Desktop/stock_valuation/netease_operating_income.csv"

class Network:

    def fetchData(self):
        r = requests.get(url = URL)
        # extracting data in json format
        data = r.json()
        return data

    def parseData(self,json):
        json['chart_data']






def main():
    # example = Network()
    # marke_cap = example.fetchData()['chart_data'][0][0]['raw_data']

    cap_info = MarcoTrendsApi().fetchMarketCapInfo("NTES")

    # read market cap data from api
    x_val = [x for x in cap_info[0]]
    y_val = [x * 1000 for x in cap_info[1]]## in million usd

    utilityTool = RevUtility()

    revenueList = utilityTool.generateRevenuefromCsv(CSV_LOCATION)

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
    py.plot(data, filename = company)







if __name__ == "__main__":
    main()
