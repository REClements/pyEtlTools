""" A tool to loop through a directory and combine files

    1.Could be modified to search for a read differnt file types
        -Change lines 17 *.csv for file type and line 26 to read specific type
    2. Parameter in pd.read_csv for files with a variable # of columns

    Author: Bob Clements 
    github: REClements
"""
import os
import glob
import pandas

myPath = input("Enter dir ")
#note 1
fileSearch = myPath+"*.csv"
#note 2
numCols=list(range(0,25))
appended_data = []

for file in glob.glob(fileSearch):

    data = pandas.read_csv(file,header=None,names=numCols)
    #data = pandas.read_csv(file)
    data['filename'] = os.path.basename(file)
    print(file)
    # print(data)
    appended_data.append(data)

appended_data = pandas.concat(appended_data)
appended_data.to_excel('combineCSV.xlsx')
