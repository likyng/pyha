# timezone hausaufgabe
# https://github.com/likyng/pyha/blob/master/timezone.py

def readCountryMap():
    import csv

    # context manager takes care of closing the file regardless of errors.
    with open("zone.csv", "r") as countryFile:
        countryData = countryFile.readlines()
    countries = csv.reader(countryData)
    clean_list = []    
    for country in countries:
        # to skip the first coloumn which contains not needed information
        temp = [country[1],country[2]]
        clean_list.append(temp)
    return clean_list

def numzones_per_country():
    result = {}
    countries = readCountryMap()
    for element in countries:
        if str(element[0]) in result:
            result[str(element[0])] += 1
        else:
           result[str(element[0])] = 1
    print(result)

numzones_per_country()

def numzones_per_continent():
    result = {}
    continents = readCountryMap()
    for element in continents:
        if str(element[1]).split('/', maxsplit = 1)[0] in result:
            result[str(element[1]).split('/', maxsplit = 1)[0]] += 1
        else:
            result[str(element[1]).split('/', maxsplit = 1)[0]] = 1
    print(result)

numzones_per_continent()

# timezone hausaufgabe nr 2 (fortgeschrittene)


