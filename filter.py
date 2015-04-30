# filter hausaufgabe

def deduplicate(entries):
    new_list = []
    for entry in entries:
        if entry not in new_list:
            new_list.append(entry)
