import requests
import matplotlib.pyplot as plt
from math import log
import datetime
import matplotlib.dates as mdates





# api-endpoint
URL = "https://ycharts.com/charts/fund_data.json?securities=id%3AFB%2Cinclude%3Atrue%2C%2C&calcs=id%3Amarket_cap%2Cinclude%3Atrue%2C%2C&correlations=&format=real&recessions=false&zoom=5&startDate=&endDate=&chartView=&splitType=single&scaleType=linear&note=&title=&source=false&units=false&quoteLegend=true&partner=&quotes=&legendOnChart=true&securitylistSecurityId=&clientGroupLogoUrl=&displayTicker=false&ychartsLogo=True&useEstimates=false&maxPoints=630"

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


    x_val = [x[0] for x in marke_cap]
    y_val = [x[1] for x in marke_cap]

    x_in_date = [datetime.datetime.fromtimestamp(x[0] / 1000.0).strftime('%Y-%m') for x in marke_cap]


    fig, ax = plt.subplots()

    plt.figure(1)
    plt.xticks(x_val, x_in_date)

    plt.plot(x_val,y_val,"g")
    ax.xaxis_date()
    fig.autofmt_xdate()
    plt.show()

    # dates = mdates.num2date(mdates.datestr2num(x_in_date[0]))
    # print dates





if __name__ == "__main__":
    main()
