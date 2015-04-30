def readCountryMap():
    import csv

    # context manager takes care of closing the file regardless of errors.
    with open("zone.csv", "r") as countryFile:
        countryData = countryFile.readlines()
    return dict(csv.reader(countryData))

def numzones_per_country():
    dict = {}
    countries = readCountryMap()
    for element in countries:
        dict[element] = {element: + 1}

    print(dict)

numzones_per_country()

#def numzones_per_continent():
    
