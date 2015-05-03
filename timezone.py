# timezone hausaufgabe
# https://github.com/likyng/pyha/blob/master/timezone.py

def readFile(filename):
    import csv

    # context manager takes care of closing the file regardless of errors.
    try:
        with open(filename, "r") as file:
            data = file.readlines()
    except IOError:
        print("Die Datei existiert nicht")
    except ValueError as e:
        print("Die Daten lassen sich nicht korrekt verarbeiten:", e)
    except:
        print("Irgendetwas anderes lief schief")
        
    readData = csv.reader(data)
    #transform in list
    list = []
    for entry in readData:
        list.append(entry)
    return list


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
    
    #read needed files
    timezones = readFile("timezone.csv")
    zone = readFile("zone.csv")
    country = dict(readFile("country.csv"))
    
    temp = [int(timezones[0][0]), timezones[0][2]]
    for region in timezones:
        #if latest timezone found, skip future entries
        if int(region[0]) < temp[0]:
            continue
        #if no time for timezone specified, skip
        elif region[2] == "":
            continue
        #checking if entry is older than time()
        elif int(region[0]) == temp[0] and float(region[2]) <= time.time():
            temp[1] = region[2]
        #if newer than time(), use entry from step before
        elif int(region[0]) == temp[0] and float(region[2]) >= time.time():
            if str(region[1]) in result:
                result[str(region[1])] += ", %s" % \
                    country[(zone[temp[0]-1][1])]
                #replaces the abbreviation with the complete name
            else:
                result[str(region[1])] = country[zone[temp[0]-1][1]]
            temp[0] += 1 #going to next ID
        #last entry is older than time() and will be used
        else:
            temp[1] = region[2]
            if str(region[1]) in result:
                result[str(region[1])] += ", %s" % \
                    country[(zone[temp[0]-1][1])]
            else:
                result[str(region[1])] = country[zone[temp[0]-1][1]]
            temp[0] += 1
            
    print(result)
    
zone_countries()
