# timezone hausaufgabe
# https://github.com/likyng/pyha/blob/master/timezone.py

import csv

def readFile(fileName):

    # context manager takes care of closing the file regardless of errors.
    with open(fileName, "r") as openedFile:
        fileData = openedFile.readlines()
    data = csv.reader(fileData)
    dataList = []    
    for entry in data:
        #temp = [country[col1],country[col2]]
        dataList.append(entry)
    return dataList

def numzones_per_country():
    result = {}
    countries = readFile("zone.csv")
    for element in countries:
        if str(element[1]) in result:
            result[str(element[1])] += 1
        else:
           result[str(element[1])] = 1
    print(result)

numzones_per_country()

def numzones_per_continent():
    result = {}
    continents = readFile("zone.csv")
    for element in continents:
        if str(element[2]).split('/', maxsplit = 1)[0] in result:
            result[str(element[2]).split('/', maxsplit = 1)[0]] += 1
        else:
            result[str(element[2]).split('/', maxsplit = 1)[0]] = 1
    print(result)

numzones_per_continent()

# timezone hausaufgabe nr 2 (fortgeschrittene)
def zone_countries():
    import time
    result = {}
    timezones = readFile("timezone.csv")
    countryMap = readFile("country.csv")
    continentMap = readFile("zone.csv")
    for element in timezones:
        # to skip timezoneless entries
        if element[2] == "":
            continue
        if str(element[1]) in result:
            # wenn die bloß die ID noch nicht in dem result dict ist, conditions checken & ggf appenden
            if str(element[0]) not in result[str(element[1])] and int(element[2]) <= time.time():
                if int(element[3]) > time.time():
                    result[str(element[1])].append(str(element[0]))
                elif int(element[3]) == 0:
                    result[str(element[1])].append(str(element[0]))
        elif float(element[2]) <= time.time():
            if int(element[3]) > time.time():
                result[str(element[1])] = [element[0]]
            elif int(element[3]) == 0:
                result[str(element[1])] = [element[0]]
    # missing: replace ID's with the corresponding country name found in zone.csv

    print(result)

zone_countries()

