import csv

with open('software.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(f"{row['name']} has {row['users']} users")