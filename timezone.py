# timezone hausaufgabe
# https://github.com/likyng/pyha/blob/master/timezone.py

def readFile(filename):
    import csv

    # context manager takes care of closing the file regardless of errors.
    with open(filename, "r") as file:
        data = file.readlines()
    return csv.reader(data)


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
    zone = readFile("zone.csv")
    temp = [timezones[0][0], timezones[0][2]]
#    for i, zone in enumerate(timezones):
    for region in timezones:
        if region[2] <= time.time() and region[0] == temp[0]:
            temp[1] = region[2]
        elif region[0] == temp[0] and region[2] >= time.time():
            if str(temp[0]) in result:
                result[str(region[1])] += ", %s" % (zone[temp[0][1]])
            else:
                result[str(region[1])] = zone[temp[0]][1]
            temp[0] += 1
        else:
            temp[1] = region[2]
            if str(temp[0]) in result:
                result[str(region[1])] += ", %s" % (zone[temp[0][1]])
            else:
                result[str(region[1])] = zone[temp[0]][1]
            temp[0] += 1
            
    print(result)
    
zone_countries()
