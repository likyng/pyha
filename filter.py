# filter hausaufgabe

def deduplicate(entries):
    new_list = []
    for entry in entries:
        if entry not in new_list:
            new_list.append(entry)
    return new_list
    
test=deduplicate([1,2,3,4,2,5])
print test