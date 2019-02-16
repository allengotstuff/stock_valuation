import sys
sys.path.append("/Users/allensun/git/stock_valuation")
from Utility import RevUtility
import datetime
from termcolor import colored
import unittest


class UtilityTestCase(unittest.TestCase):


    def setUp(self):
        self.revUtility = RevUtility()
        self.revList = self.revUtility.generateRevenuefromCsv("/Users/allensun/git/stock_valuation/test/fb_rev.csv")

    def tearDown(self):
        self.utility = None
        self.revList = None

    def test(self):
        test_data_1 = datetime.datetime(2016, 2, 1)
        rev = self.revUtility.findRevenueForGiveDate(test_data_1,self.revList)

    def test_2(self):
        test_data_2 = datetime.datetime(2010, 9, 27)
        rev = self.revUtility.findRevenueForGiveDate(test_data_2,self.revList)
        self.assertEquals(rev[0], datetime.datetime(2010, 6, 30))

    def test_3(self):
        test_data_3 = datetime.datetime(2011, 10, 8)
        rev = self.revUtility.findRevenueForGiveDate(test_data_3,self.revList)
        self.assertEquals(rev[0], datetime.datetime(2011, 9, 30))

    def test_4(self):
        test_data_4 = datetime.datetime(2022, 4, 26)
        rev = self.revUtility.findRevenueForGiveDate(test_data_4,self.revList)
        self.assertEquals(rev[0], self.revList[len(self.revList) -1][0])

    def test_5(self):
        test_data_5 = datetime.datetime(2006, 2, 1)
        rev = self.revUtility.findRevenueForGiveDate(test_data_5,self.revList)
        self.assertEquals(rev, None)

    def test_6(self):
        test_data_6 = datetime.datetime(2007, 12, 1)
        rev = self.revUtility.findRevenueForGiveDate(test_data_6,self.revList)
        self.assertEquals(rev, None)

    def test_7(self):
        test_data_8 = datetime.datetime(2020, 12, 1)
        rev = self.revUtility.findRevenueForGiveDate(test_data_8,self.revList)
        self.assertEquals(rev[0], self.revList[len(self.revList) -1][0])


    def test_convertStringToDate(self):
        utily = RevUtility()
        date = utily.convertToDate("Q3 2017")
        target = datetime.datetime(2017, 9, 30)
        self.assertEquals(date, target)



if __name__ == "__main__":
    unittest.main()
