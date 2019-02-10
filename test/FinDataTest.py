import sys
sys.path.append("/Users/allensun/git/stock_valuation")
from FinDataApi import MarcoTrendsApi
import unittest
import json
import datetime


class MarcoTrendsApiTestCase(unittest.TestCase):

    def setUp(self):
        f = open("/Users/allensun/git/stock_valuation/test/MarcoTrendsApi.txt", "r")
        bench_info =  f.read()
        dirList = json.loads(bench_info)

        self.marcoApi = MarcoTrendsApi()
        self.capInfo = self.marcoApi.fetchMarketCapInfo("FB")
        self.benchInfo = dirList

    def tearDown(self):
        self.marcoApi = None
        self.capInfo = None
        self.benchInfo = None

    def test_cap_size(self):
        self.assertEquals(len(self.capInfo[0]),len(self.capInfo[1]))
        self.assertEquals(len(self.capInfo[0]),len(self.benchInfo))

    def test_cap_0(self):

        position = 0

        _ = str(self.benchInfo[position]["date"]).split("-")
        year = _[0]
        month = _[1].lstrip('0')
        date = _[2].lstrip('0')

        benchTimeStamp = datetime.datetime(int(year), int(month), int(date))
        benchCap = float(self.benchInfo[position]["v1"])

        print benchTimeStamp
        print benchCap

        self.assertEquals(benchTimeStamp,self.capInfo[0][position] )
        self.assertEquals(benchCap,self.capInfo[1][position])

    def test_cap_1(self):

        position = 300

        _ = str(self.benchInfo[position]["date"]).split("-")
        year = _[0]
        month = _[1].lstrip('0')
        date = _[2].lstrip('0')

        benchTimeStamp = datetime.datetime(int(year), int(month), int(date))
        benchCap = float(self.benchInfo[position]["v1"])

        print benchTimeStamp
        print benchCap

        self.assertEquals(benchTimeStamp,self.capInfo[0][position] )
        self.assertEquals(benchCap,self.capInfo[1][position])

    def test_cap_2(self):
        position = len(self.benchInfo) -1
        _ = str(self.benchInfo[position]["date"]).split("-")
        year = _[0]
        month = _[1].lstrip('0')
        date = _[2].lstrip('0')

        benchTimeStamp = datetime.datetime(int(year), int(month), int(date))
        benchCap = float(self.benchInfo[position]["v1"])

        print benchTimeStamp
        print benchCap

        self.assertEquals(benchTimeStamp,self.capInfo[0][position] )
        self.assertEquals(benchCap,self.capInfo[1][position])

    def test_cap_3(self):
        position =  -1
        _ = str(self.benchInfo[position]["date"]).split("-")
        year = _[0]
        month = _[1].lstrip('0')
        date = _[2].lstrip('0')

        benchTimeStamp = datetime.datetime(int(year), int(month), int(date))
        benchCap = float(self.benchInfo[position]["v1"])

        print benchTimeStamp
        print benchCap

        self.assertEquals(benchTimeStamp,self.capInfo[0][position] )
        self.assertEquals(benchCap,self.capInfo[1][position])









if __name__ == "__main__":
    unittest.main()
