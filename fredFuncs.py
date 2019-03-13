from datetime import datetime

def handlePeriods(value):

    try:
        return float(value)

    except:
        return float('NaN')


def makeDateTime(strDate):
    splitDate = strDate.split('-')
    year = int(splitDate[0])
    if splitDate[1][0] == str(0):
        month = int(splitDate[1][1])
    else:
        month = int(splitDate[1])
    if splitDate[2][0] == str(0):
        day = int(splitDate[2][1])
    else:
        day = int(splitDate[2])
    dt = datetime(year, month, day)
    return dt

