class Student():
    
    university='UEK Kraków'
    album_nr=100000
    
    def __init__(self, name, surname, studies):
        self.name = name
        self.surname = surname
        self.studies = studies
        self.id=Student.album_nr
        Student.album_nr+=1
        
        new_name=''
        is_first=True
        new_surname=''
        for letter in name:
            if is_first:
                new_name += letter.upper()
                is_first=False
            else:
                new_name += letter.lower()
        for letter in surname:
            new_surname += letter.upper()
        
        self.name=new_name
        self.surname=new_surname
    
    def __str__(self):
        return f"{self.name} {self.surname} ({self.id}), {self.studies}, {Student.university}"
    
student1=Student('Anna','May','Applied Informatics')
print(student1)
student2=Student('Dariusz','Szyszlak','Applied Informatics')
print(student2)
student3=Student('Gocha','Lis','Applied Informatics')
print(student3)
        