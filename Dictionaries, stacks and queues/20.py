import json
#kopiowanie kontentu z jednego do drugiego bez obostrzeń
#open("limited.json", "w").write(open("students.json").read())

with open("students.json", "r") as file:
    students = json.load(file)
    for student in students:
        del student["gender"]
        del student["year_of_study"]
        del student["email"]
        
    with open("limited.json","w") as limited:
        json.dump(students,limited)
    
        

