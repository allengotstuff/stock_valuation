import requests
from lxml import html
import re
import json
import datetime
from Utility import RevUtility

class MarcoTrendsApi:

    __MARKET_CAP_BASE_URL = "https://www.macrotrends.net/assets/php/market_cap.php?t="

    __REVENUE_BASE_URL = "https://www.macrotrends.net/stocks/charts"

    def _constructUrlForMarketCap(self, company_symbol):
        """construct url to fetch target company's market cap"""
        return self.__MARKET_CAP_BASE_URL + company_symbol

    def _convertJsonToTupleOfList(self,payloadString):
        """convert the json array of (marketcap, data) to tuple of ((marketcap in million), (timeStamp))"""
        dirList = json.loads(payloadString)
        ## market cap information
        market_cap = []
        timeStamp = []

        for item in dirList:
            _ = str(item["date"]).split("-")
            year = _[0]
            month = _[1].lstrip('0')
            date = _[2].lstrip('0')

            cap_date = datetime.datetime(int(year), int(month), int(date))

            timeStamp.append(cap_date)
            market_cap.append(float(item["v1"]))

        return (tuple(timeStamp),tuple(market_cap))

    def fetchMarketCapInfo(self, company_symbol):
        targetUrl = self._constructUrlForMarketCap(company_symbol)
        pageContent = requests.get(url = targetUrl)
        tree = html.fromstring(pageContent.content)
        scriptData = tree.xpath('/html/body/script[contains(., sdfasdf)]/text()')[0]
        p = re.compile("var chartData = (.*?);")

        ##find the script json data in string
        chartData = p.search(str(scriptData)).groups()[0]
        return self._convertJsonToTupleOfList(chartData)

    def fetchRevenueInfo(self, company_symbol, company_name):
        """return the list of tuple with company revenu from in ascending timeline """
        result = []
        utility = RevUtility()

        url = self.__REVENUE_BASE_URL + "/" + company_symbol + "/" + company_name + "/revenue"
        pageContent = requests.get(url = url)
        tree = html.fromstring(pageContent.content)
        table = tree.xpath('//*[@id="style-1"]/div[2]/table/tbody/tr')

        for item in table:
            data = item.xpath('td/text()')

            date = utility.convertToDate(data[0])
            revenue = float(data[1].replace(",", "").replace("$",""))
            result.append((date,revenue))

        result.reverse()
        return result






if __name__ == "__main__":

    MarcoTrendsApi().fetchRevenueInfo("FB","facebook")

    # print MarcoTrendsApi().fetchMarketCapInfo("FB")
