from ..Utility import MauUtility
import datetime
from termcolor import colored






def test():
    mauTool = MauUtility()
    mau_list = mauTool.generateMAUfromCsv("/Users/allensun/Desktop/stock_valuation/fb_mau.csv")


    test_data_1 = datetime.datetime(2016, 2, 1)
    mau_date = mauTool.findMauForGiveDate(test_data_1,mau_list)
    print "2016, 2, 1 ==>" + str(mau_date)
    if mau_date[0] == datetime.datetime(2015, 12, 31):
        print colored('pass','green')
    else:
        print colored('failed', 'red')

    test_data_2 = datetime.datetime(2009, 9, 27)
    mau_date = mauTool.findMauForGiveDate(test_data_2,mau_list)
    print "2009, 9, 27 ==>" + str(mau_date)
    if mau_date[0] == datetime.datetime(2009, 6, 30):
        print colored('pass','green')
    else:
        print colored('failed', 'red')

    test_data_3 = datetime.datetime(2011, 10, 8)
    mau_date = mauTool.findMauForGiveDate(test_data_3,mau_list)
    print "2011, 10, 8 ==>" + str(mau_date)
    if mau_date[0] == datetime.datetime(2011, 9, 30):
        print colored('pass','green')
    else:
        print colored('failed', 'red')

    test_data_4 = datetime.datetime(2022, 4, 26)
    mau_date = mauTool.findMauForGiveDate(test_data_4,mau_list)
    print "2022, 4, 26 ==>" + str(mau_date)
    if mau_date[0] == datetime.datetime(2019, 2, 1):
        print colored('pass','green')
    else:
        print colored('failed', 'red')

    test_data_5 = datetime.datetime(2006, 2, 1)
    mau_date = mauTool.findMauForGiveDate(test_data_5,mau_list)
    print "2006, 2, 1 ==>" + str(mau_date)
    if mau_date == None:
        print colored('pass','green')
    else:
        print colored('failed', 'red')

    test_data_6 = datetime.datetime(2007, 12, 1)
    mau_date = mauTool.findMauForGiveDate(test_data_6,mau_list)
    print "2007, 12, 1 ==>" + str(mau_date)
    if mau_date == None:
        print colored('pass','green')
    else:
        print colored('failed', 'red')

    test_data_8 = datetime.datetime(2020, 12, 1)
    mau_date = mauTool.findMauForGiveDate(test_data_8,mau_list)
    print "2020, 12, 1 ==>" + str(mau_date)
    if mau_date[0] == datetime.datetime(2019, 2, 1):
        print colored('pass','green')
    else:
        print colored('failed', 'red')

    test_data_9 = datetime.datetime(2019, 2, 3)
    mau_date = mauTool.findMauForGiveDate(test_data_9,mau_list)
    print "2019, 2, 3 ==>" + str(mau_date)
    if mau_date[0] == datetime.datetime(2019, 2, 1):
        print colored('pass','green')
    else:
        print colored('failed', 'red')








if __name__ == "__main__":
    test()
