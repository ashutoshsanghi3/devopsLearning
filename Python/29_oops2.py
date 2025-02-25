class Person:
    def __init__(self,fname='default_name',age=0):
        self.fname=fname
        self.age=age
        self.skills=[]
    
    def printing(self):
        return f'Name: {self.fname}\nAge: {self.age}\nSkills: {self.skills}'
    
    def skills_insertion(self,skill):
        self.skills.append(skill)

class Student(Person):
    def __init__(self, fname='default_name', age=0,studentId=0):
        super().__init__(fname, age)
        self.studentId=studentId
    def printing(self):
        return super().printing()+f'\nStudentId: {self.studentId}'

s1=Student("Ram",21,101)
# print(s1)
# print(s1.printing())