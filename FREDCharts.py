from bokeh.plotting import output_file, figure, show

output_file('FREDCharts.html')

def 

    seriesData[id]['values'] = [ff.handlePeriods(observation['value'])
                                for observation 
                                in content['observations']]
    seriesData[id]['dates'] = [ff.makeDateTime(observation['date'])
                               for observation
                               in content['observations']]