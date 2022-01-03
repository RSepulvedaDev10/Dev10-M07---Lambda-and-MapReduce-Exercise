import csv
import json
from functools import reduce

data = []
neighborhoods = []

with open('911_Calls_for_Service_(Last_30_Days).csv') as csvFile:
    data = [{x: y for x,y in row.items()} for row in csv.DictReader(csvFile)]
        
data = list(filter(lambda x: x["zip_code"] != "0" and x["neighborhood"] != "" and x["dispatchtime"] != "" and x["totaltime"] != "" and x["totalresponsetime"] != "", data))


avgTotalResponseTime = reduce(lambda x,y: x + y, list(map(lambda x: float(x["totalresponsetime"]),data)))/len(data)
avgDispatchTime = reduce(lambda x,y: x + y, list(map(lambda x: float(x["dispatchtime"]),data)))/len(data)
avgTotalTime = reduce(lambda x,y: x + y, list(map(lambda x: float(x["totaltime"]),data)))/len(data)


print(f"Average Total Response Time: {avgTotalResponseTime}")
print(f"Average Dispatch Time: {avgDispatchTime}")
print(f"Average Total Time: {avgTotalTime}")


for x in data:
       if x["neighborhood"] not in neighborhoods:
            neighborhoods.append(x["neighborhood"])
    

NeighborhoodData = []

for neighborhood in neighborhoods:
    length = len(list(filter(lambda x: x["neighborhood"] == neighborhood,data)))
    cleanedList = list(filter(lambda x: x["neighborhood"] == neighborhood,data))
    
    avgTotalResponseTime = reduce(lambda x,y: x + y, list(map(lambda x: float(x["totalresponsetime"]),cleanedList)))/length
    avgDispatchTime = reduce(lambda x,y: x + y, list(map(lambda x: float(x["dispatchtime"]),cleanedList)))/length
    avgTotalTime = reduce(lambda x,y: x + y, list(map(lambda x: float(x["totaltime"]),cleanedList)))/length

    print(f"\n{neighborhood}\n")
    print(f"Average Total Response Time: {avgTotalResponseTime}")
    print(f"Average Dispatch Time: {avgDispatchTime}")
    print(f"Average Total Time: {avgTotalTime}")
    
    formattedList = {"Neighborhood": neighborhood, "Average Total Response Time": avgTotalResponseTime, "Average Dispatch Time": avgDispatchTime, "Average Total Time": avgTotalTime}
    NeighborhoodData.append(formattedList)
 
  
with open("Lambda and MapReduce Exercise.json", "w") as jsonFile:
    jsonObject = json.dump(NeighborhoodData, jsonFile)
    jsonFile.write(jsonObject)