import json

student={"Name":"Yoon Oh",
          "Surname":"Jeong",
          "Birthday": {"Month":"February","Day":14},
          "Birthyear":1997,
          "Address":{"Street_name":"ABCabc", "House_num":22, "Flat_num":None},
          "Male":True,
          "Grade":4,
          "Major":"Music production"
          }

with open('student.json','w') as file:
    json.dump(student, file, indent=4)
    file.close()
########reading   
with open("student.json") as file:
    data = json.load(file)
for k,v in data.items():
    print(k,":",v)