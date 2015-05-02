# timezone hausaufgabe
# https://github.com/likyng/pyha/blob/master/timezone.py

import csv

def readFileMap(fileName, col1, col2):

    # context manager takes care of closing the file regardless of errors.
    with open(fileName, "r") as countryFile:
        countryData = countryFile.readlines()
    countries = csv.reader(countryData)
    clean_list = []    
    for country in countries:
        # to skip the first coloumn which contains not needed information
        temp = [country[col1],country[col2]]
        clean_list.append(temp)
    return clean_list

def numzones_per_country():
    result = {}
    countries = readFileMap("zone.csv", 1, 2)
    for element in countries:
        if str(element[0]) in result:
            result[str(element[0])] += 1
        else:
           result[str(element[0])] = 1
    print(result)

#numzones_per_country()

def numzones_per_continent():
    result = {}
    continents = readFileMap("zone.csv", 1, 2)
    for element in continents:
        if str(element[1]).split('/', maxsplit = 1)[0] in result:
            result[str(element[1]).split('/', maxsplit = 1)[0]] += 1
        else:
            result[str(element[1]).split('/', maxsplit = 1)[0]] = 1
    print(result)

print("\n")
#numzones_per_continent()

# timezone hausaufgabe nr 2 (fortgeschrittene)
def zone_countries():
    result = {}
    timezones = readFileMap("timezone.csv", 0, 1)
    for element in timezones:
        if str(element[1]) in result:
            # wenn die ID noch nicht in der liste 
            if str(element[0]) not in result[str(element[1])]:
                result[str(element[1])].append(str(element[0]))

        else:
            result[str(element[1])] = [element[0]]

    print(result)

zone_countries()



