import requests
import matplotlib.pyplot as plt
from math import log
import datetime
import matplotlib.dates as mdates

from Utility import MauUtility
import plotly.graph_objs as go
import plotly.plotly as py





# api-endpoint
URL = "https://ycharts.com/charts/fund_data.json?securities=id%3AFB%2Cinclude%3Atrue%2C%2C&calcs=id%3Amarket_cap%2Cinclude%3Atrue%2C%2C&correlations=&format=real&recessions=false&zoom=10&startDate=&endDate=&chartView=&splitType=single&scaleType=linear&note=&title=&source=false&units=false&quoteLegend=true&partner=&quotes=&legendOnChart=true&securitylistSecurityId=&clientGroupLogoUrl=&displayTicker=false&ychartsLogo=&useEstimates=false&maxPoints=576"

class Network:

    def fetchData(self):
        r = requests.get(url = URL)
        # extracting data in json format
        data = r.json()
        return data

    def parseData(self,json):
        json['chart_data']






def main():
    example = Network()
    marke_cap = example.fetchData()['chart_data'][0][0]['raw_data']

    # read market cap data from api
    x_val = [datetime.datetime.fromtimestamp(x[0]/1000) for x in marke_cap]
    y_val = [x[1] for x in marke_cap]

    mau_tool = MauUtility()

    mau_list = mau_tool.generateMAUfromCsv("/Users/allensun/Desktop/stock_valuation/fb_data.csv")

    # create values  per user list
    values_per_user_list = []

    paybackTime = []
    for i in range(len(x_val)):
        cap = y_val[i]

        current_date = x_val[i]

        current_mau = mau_tool.findMauForGiveDate(current_date, mau_list)[1]

        values_per_user_list.append(cap/current_mau)

        current_rev = mau_tool.findMauForGiveDate(current_date, mau_list)[2]

        revenue_per_user = current_rev/float(current_mau)

        paybackTime.append( (cap/current_mau) / revenue_per_user)

    data = [go.Scatter(x=x_val, y=paybackTime)]
    py.plot(data, filename = 'time-series-simple')







if __name__ == "__main__":
    main()
