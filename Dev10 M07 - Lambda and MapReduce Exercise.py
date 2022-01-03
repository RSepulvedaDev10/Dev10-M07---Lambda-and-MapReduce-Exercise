import csv
import json
from functools import reduce

data = list()

with open('911_Calls_for_Service_(Last_30_Days).csv') as csvFile:
    csvReader = csv.DictReader(csvFile)
    for line in csvReader:
        data.append(line)
        
cleanerData = filter(lambda x: False if (x['zip_code'] is '0') or (x['neighborhood'] is '') else True, data)

print(cleanerData)
