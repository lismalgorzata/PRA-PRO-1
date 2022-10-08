class Person():
    def __init__(self,name, surname):
        self.name = name
        self.surname= surname
    def greet(self):
        print(f'Hello everyone! I\'m {self.name} {self.surname}')

class Teacher(Person):
    def __init__(self,name,surname,university):
        self.university = university
        super().__init__(name, surname)
    def say(self):
        print(f'I work as a teacher at {self.university}')
    def bye(self):
        print(f'And now {self.name} {self.surname} is telling you goodbye!')
        
t = Teacher('Johnny','Metal','UEK')
t.greet()
t.say()
t.bye()
