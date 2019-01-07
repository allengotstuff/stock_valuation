import requests
import matplotlib.pyplot as plt
from math import log
import datetime
import matplotlib.dates as mdates
import csv
from DateUtility import DateUntiles
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


    # read mau data from csv file
    mau_list = []
    with open("/Users/allensun/Desktop/stock_valuation/fb_mau.csv", "rb") as f:
        reader = csv.reader(f)
        converter = DateUntiles()

        for i in range(3): # skipp the first 3 rows that contains documentation
            next(reader)

        for i, line in enumerate(reader):
            mau_date =  converter.convertToDate(line)
            mau_count = int(line[1].replace(",", ""))

            mau_list.append((mau_date,mau_count))

        # since we don't have the mau data for the last quarter, we are using the consarvation number
        mau_list.append((datetime.datetime(2019, 2, 1),2271))

        # print mau_list

    # create values  per user list
    values_per_user_list = []

    for i in range(len(x_val)):
        cap = y_val[i]

        current_date = x_val[i]

        current_mau = 0

        for i in range(len(mau_list)):
            timeStamp = mau_list[i][0]
            if current_date > timeStamp:
                continue
            else :
                current_mau = mau_list[i-1][1]
                break
        values_user = cap/current_mau
        values_per_user_list.append(values_user)

    data = [go.Scatter(x=x_val, y=values_per_user_list)]
    py.plot(data, filename = 'time-series-simple')







if __name__ == "__main__":
    main()
