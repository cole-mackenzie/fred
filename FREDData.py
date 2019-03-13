import requests
import time

import fredFuncs as ff

file = 'fredAPIKey.txt'
with open(file, 'r') as f:
    apiKey = '&api_key=' + f.read()

fileType = '&file_type=json'

seriesIDs = ['T5YIE', 'USEPUINDXD']

baseURL = 'https://api.stlouisfed.org/fred/series/observations?series_id='

seriesData = {}

inflationURL = finalURL = baseURL + seriesIDs[0] + apiKey + fileType
uncertaintyURL = finalURL = baseURL + seriesIDs[1] + apiKey + fileType

inflationPage = requests.get(inflationURL)
inflationDict = inflationPage.json()
time.sleep(3)
uncertaintyPage = requests.get(uncertaintyURL)
uncertaintyDict = uncertaintyPage.json()


