#1
items = [3, 5, 7, 9, 11, 13]

removed = items.pop(4)   # removes 11

items.insert(1, removed) # add at 2nd position
items.append(removed)    # add at end

print(items)


#2
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

common = first_set.intersection(second_set)

print("Common elements:", common)

first_set = first_set - common

print("Updated first_set:", first_set)

#3
first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

if first_set.issubset(second_set):
    print("first_set is subset of second_set")

    for i in first_set.copy():
        second_set.remove(i)

    print("Updated second_set:", second_set)

elif first_set.issuperset(second_set):
    print("first_set is superset of second_set")

    for i in second_set.copy():
        first_set.remove(i)

    print("Updated first_set:", first_set)

else:
    print("No subset/superset relation")


#4
month = { 'jan': 47,'feb': 52,'march': 47, 'April': 44,'May': 52,'June': 53,'july': 54,
            'Aug': 44,'Sept': 54 }
values = list(set(month.values()))
print(values)

#5
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
unique = tuple(set(sample_list))
print("Tuple:", unique)
print("Minimum:", min(unique))
print("Maximum:", max(unique))

#6
club_A = {"ram", "hari", "shyam"}
club_B = {"ram", "gita", "hari"}
common = club_A.intersection(club_B)
if common:
    print("Common members:", common)
else:
    print("No overlapping members found between groups")

#7
required_tasks = {"Email", "Report", "Meeting"}
completed_tasks = {"Email", "Report"}

if required_tasks.issubset(completed_tasks):
    print("All tasks done")
else:
    pending = required_tasks - completed_tasks
    print("Some tasks pending")
    print("Pending tasks:", pending)
