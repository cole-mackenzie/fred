import pandas as pd
import time
import fred.series as fs

seriesIDs = ['UR', 'LF']

# empty Dict
dict = {}

with open('fredAPIKey.txt', 'r') as f:
    apiKey = f.read()

abbrevs = pd.read_csv('Abbrevs.csv')

for state in abbrevs.Abbrev:
    print(state)
    dict[state] = {}
    for i in seriesIDs:
        dict[state][i] = {}
        id = state + i
        stateData = fs.fredSeries(apiKey, id)
        dict[state][i]['Date'] = stateData.xValues
        dict[state][i]['Value'] = stateData.yValues
    time.sleep(.5)