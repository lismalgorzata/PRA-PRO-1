import csv
with open('csv.csv', newline='') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        if int(row['age'])<30:
            print(row['first_name'], '\t '+row['last_name'], '\t'+row['email'])
            
