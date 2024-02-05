import os
import shutil
import time

directory = 'project'
archiveFolder = 'archive'

def append_timestamp(filename):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    return "{0}_{2}.{1}".format(*filename.rsplit('.', 1) + [timestr])

def validateFile(contents):
    for item in contents:
        print(item)
        #open each folder and check file name
        folder = os.listdir(directory+'/'+item)
        print(folder)
        #validate file name has date month?
        #-----write code for validate file name here
        #if file exists, then move the file to archive
        for eachFile in folder:
            src = directory+'/'+item+'/'+eachFile
            print(src)
            newSrc = append_timestamp(src)
            os.rename(src, newSrc)
            print(newSrc)
            print(archiveFolder)
            shutil.move(newSrc, archiveFolder)


if not os.path.exists(archiveFolder):
    os.makedirs(archiveFolder)

if os.path.exists(directory):
    contents = os.listdir(directory)

validateFile(contents=contents)