from calendar import monthrange
import datetime
import csv

class MauUtility:

    QUARTER_TO_MONTH = {
        'Q1': 3,
        'Q2': 6,
        'Q3': 9,
        'Q4': 12
        }

    def generateMAUfromCsv(self, fiel_location):
        """open the csv file in file location, and generate list of tuple (datetime, mau) """
        # read mau data from csv file
        mau_list = []
        with open(fiel_location, "rb") as f:
            reader = csv.reader(f)

            for i in range(3): # skipp the first 3 rows that contains documentation
                next(reader)

            for i, line in enumerate(reader):
                mau_date =  self.convertToDate(line)
                mau_count = int(line[1].replace(",", ""))
                revenue = int(line[2].replace(",", ""))

                mau_list.append((mau_date,mau_count,revenue))

            # since we don't have the mau data for the last quarter, we are using the consarvation number
            mau_list.append((datetime.datetime(2019, 2, 1),2271,13727))
        return mau_list


    def findMauForGiveDate(self,current_date, mau_list):
        # find the matching mau for the give date
        # need to write unit test for this
        pos = -1

        for i in range(len(mau_list)):

            if i==0 and current_date < mau_list[i][0]:
                return None


            timeStamp = mau_list[i][0]
            if current_date > timeStamp:
                continue
            elif current_date == timeStamp:
                pos = i
                break
            else:
                pos = i - 1
                break

        if pos < 0:
            # return the last index of loop does find anything
            return mau_list[len(mau_list) -1]
        else:
            return mau_list[pos]



    def convertToDate(self,list):
        # ["Q3 '17", '2,072']
        format_list = list[0].replace(" ", "").split('\'')

        #convert to ['Q3', '17']
        year = int('20' + format_list[1])

        month = self.QUARTER_TO_MONTH.get(format_list[0])

        date = monthrange(year, month)[1]

        # return date object
        return datetime.datetime(year, month, date)
