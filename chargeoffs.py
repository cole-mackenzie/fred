for link in links:
    print(link)
    page = requests.get(link)
    time.sleep(5)
    with open(tempXml, 'wb') as f:
        f.write(page.content)
    page = None
    data = jsonToDict.jsonToDict(tempXml)
    df = pd.DataFrame(data=data)
    df = df[df['{http://www.sec.gov/edgar/document/absee/autoloan/assetdata}zeroBalanceCode'] == '4']
    existingDf = pd.read_csv(r'c:\users\dcsma\documents\amcar.csv')
    allDFs = [df, existingDf]
    newDF = pd.concat(allDFs)
    newDF.to_csv(r'c:\users\dcsma\documents\amcar.csv')
