person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }
>>> person
{'name': 'Marek', 'surname': 'Banach', 'age': 25, 'hobby': ['swimming', 'excursions'], 'married': True, 'phone': {'landline': '123444321', 'mobile': '777888999'}}
>>> person["name"]
'Marek'
>>> person["hobby"]
['swimming', 'excursions']
>>> person["surname"]=Nowak
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'Nowak' is not defined
>>> person["surname"]="Nowak"
>>> person
{'name': 'Marek', 'surname': 'Nowak', 'age': 25, 'hobby': ['swimming', 'excursions'], 'married': True, 'phone': {'landline': '123444321', 'mobile': '777888999'}}
>>> person["married"]=False
>>> person
{'name': 'Marek', 'surname': 'Nowak', 'age': 25, 'hobby': ['swimming', 'excursions'], 'married': False, 'phone': {'landline': '123444321', 'mobile': '777888999'}}
>>> person["married"]=not person["married"]
>>> person
{'name': 'Marek', 'surname': 'Nowak', 'age': 25, 'hobby': ['swimming', 'excursions'], 'married': True, 'phone': {'landline': '123444321', 'mobile': '777888999'}}
>>> person["married"]=not person["married"]
>>> person
{'name': 'Marek', 'surname': 'Nowak', 'age': 25, 'hobby': ['swimming', 'excursions'], 'married': False, 'phone': {'landline': '123444321', 'mobile': '777888999'}}
>>> person["gender"]="male"
>>> person
{'name': 'Marek', 'surname': 'Nowak', 'age': 25, 'hobby': ['swimming', 'excursions'], 'married': False, 'phone': {'landline': '123444321', 'mobile': '777888999'}, 'gender': 'male'}
>>> person["hobby"].append("bicycle")
>>> person
{'name': 'Marek', 'surname': 'Nowak', 'age': 25, 'hobby': ['swimming', 'excursions', 'bicycle'], 'married': False, 'phone': {'landline': '123444321', 'mobile': '777888999'}, 'gender': 'male'}
>>> person["phone"]["work"="123456789"]
  File "<pyshell>", line 1
    person["phone"]["work"="123456789"]
                          ^
SyntaxError: invalid syntax
>>> person["phone"]["work"]="123456789"
>>> person
{'name': 'Marek', 'surname': 'Nowak', 'age': 25, 'hobby': ['swimming', 'excursions', 'bicycle'], 'married': False, 'phone': {'landline': '123444321', 'mobile': '777888999', 'work': '123456789'}, 'gender': 'male'}
>>> 