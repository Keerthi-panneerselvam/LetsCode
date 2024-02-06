import pandas as pd
import os
from datetime import datetime

A = [{"file_id": "1","app_code": "cpbt","file_name":"cbpt_yyyymmdd.csv"},
    {"file_id": "2","app_code": "lobt","file_name":"lobt_yyyymmdd.csv"}]

# Create a Pandas DataFrame
df = pd.DataFrame(A)

# print(df)
print(df["app_code"])

directory = 'FileValidator/project'

def validateData(appCodeList):
    #iterate through the list and open the file based on the appCode name and validate the data
    for appCode in appCodeList:
        appCodeDirPath = directory+'/'+appCode
        directoryExists = os.path.exists(appCodeDirPath)
        if directoryExists:
            #open csv file to validate the data
            listOfFilesInDir = os.listdir(appCodeDirPath)
            #handle if no file is there
            if len(listOfFilesInDir) > 0:
                file = listOfFilesInDir[0]
                dataFromCsvFile = getDataFromCsvFile(fileName=appCodeDirPath+'/'+file)
                isFileValid = validateFileAttributes(dataFromCsvFile, appCode)
                if isFileValid:
                    print("File is valid")
                else:
                    print("File not valid")
            else:
                print("No file in directory. Directory is empty")

def getDataFromCsvFile(fileName):
    data = pd.read_csv(fileName)
    data_dict = data.to_dict(orient='records')
    return data_dict

def validateFileAttributes(data, appCode):
    valid = True
    for eachData in data:
       for key, value in eachData.items():
           valid = valid and validateAttributes(appCode, key, value)
    return valid
           
def validateAttributes(appCode, key, value):
    match key:
         case "date":
            valid = validateDate(value)
         case "app_code":
             valid = validateAppCode(value, appCode)
         case "name":
             valid = validateName(value)
         case _:
             print("No validation")
    return valid
                
def validateDate(date):
    try:
        datetime.strptime(str(date), '%Y%m%d')
        return True
    except ValueError:
        return False
    
def validateAppCode(fileAppCode, appCode):
    return fileAppCode == appCode

def validateName(name):
    return isinstance(str(name), str)

validateData(df["app_code"])

