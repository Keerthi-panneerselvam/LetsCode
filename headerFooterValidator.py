import os
import pandas as pd

countryTemplateMap = {
  "au": ["Name","age","dob"],
  "sg": ["Name","age","dob","weight"],
}

directory = 'FileValidator/project'

def read_csv(fileName):
    data = pd.read_csv(fileName)
    return (list(data.columns), data.tail(1).values.item(1), len(data.index))

def validateHeader(header, headerTemplate):
    return sorted(header) == sorted(headerTemplate) 

def validateFooter(rowsCount, countFromFooter):
    print(rowsCount)
    print(countFromFooter)
    return rowsCount == countFromFooter

def validateData(countries):
    for country in countries:
        # print(country)
        folder = os.listdir(directory+'/'+country)
        for eachFile in folder:
            src = directory+'/'+country+'/'+eachFile
            dataFromFile = read_csv(src)
            header = dataFromFile[0]
            footer = dataFromFile[1]
            countOfRows = dataFromFile[2]
            valid = validateHeader(header, countryTemplateMap[country])
            print(valid)
            valid = valid and validateFooter(countOfRows-1, footer)
            if valid:
                print("File is valid")
            else:
                print("File not valid")

validateData(["au","sg"])