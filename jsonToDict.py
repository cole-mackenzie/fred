import xml.etree.ElementTree as et
import pandas as pd

def jsonToDict(content):

    parsedContent = et.parse(content)
    tree = parsedContent.getroot()
    tags = list(set([element.tag 
                     for child in tree.findall('{http://www.sec.gov/edgar/document/absee/autoloan/assetdata}assets') 
                     for element in child]))
    data = {}
    for tag in tags:
        data[tag] = []

    for child in tree.findall('{http://www.sec.gov/edgar/document/absee/autoloan/assetdata}assets'):
        for tag in data.keys():
            if child.find(tag) == None:
                data[tag].append('')
            else:
                data[tag].append(child.find(tag).text)

    return data


