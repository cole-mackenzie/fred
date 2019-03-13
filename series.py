import requests
from datetime import datetime as dt

class fredSeries:

    def __init__(self, apiKey, seriesID):

        self.data = self.getPage(apiKey, seriesID)
        self.xValues = [
                        dt(\
                            int(dataPoint['date'][:4]),\
                            int(dataPoint['date'][5:7]),\
                            int(dataPoint['date'][8:])
                           )
                        for dataPoint
                        in self.data['observations']
                        ]
        self.yValues = [
                        float(dataPoint['value'])
                        for dataPoint 
                        in self.data['observations']
                        ]

    def getPage(self, apiKey, seriesID):

        baseURL = 'https://api.stlouisfed.org/fred/series/observations?series_id='
        format = '&file_type=json'
        finalURL = baseURL + seriesID + '&api_key=' + apiKey + format
        page = requests.get(finalURL)
        return page.json()