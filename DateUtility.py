from calendar import monthrange
import datetime

class DateUntiles:

    QUARTER_TO_MONTH = {
        'Q1': 3,
        'Q2': 6,
        'Q3': 9,
        'Q4': 12
        }

    def convertToDate(self,list):
        # ["Q3 '17", '2,072']
        format_list = list[0].replace(" ", "").split('\'')

        #convert to ['Q3', '17']
        year = int('20' + format_list[1])

        month = self.QUARTER_TO_MONTH.get(format_list[0])

        date = monthrange(year, month)[1]

        # return date object
        return datetime.datetime(year, month, date)
