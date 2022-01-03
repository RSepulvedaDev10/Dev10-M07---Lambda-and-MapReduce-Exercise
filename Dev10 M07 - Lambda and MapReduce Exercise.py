import csv

data = list()

with open('911_Calls_for_Service_(Last_30_Days).csv') as csvFile:
    csvReader = csv.DictReader(csvFile)
    for line in csvReader:
        data.append(line)
        
print(data)