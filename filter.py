# filter hausaufgabe
# https://github.com/likyng/pyha.git

def deduplicate(entries):
    new_list = []
    for entry in entries:
        if entry not in new_list:
            new_list.append(entry)
    return new_list
    
test = deduplicate([1,2,3,4,2,5])
<<<<<<< HEAD
print(test)
=======
print(test)
>>>>>>> 210f0becb38b59f9cbbc71218135f10c60fb8dba
