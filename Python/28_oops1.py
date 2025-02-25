class Person:
    def __init__(self,fname='default_name',age=0):
        self.fname=fname
        self.age=age
        self.skills=[]
    def printing(self):
        return f'Name: {self.fname}\nAge: {self.age}\nSkills: {self.skills}'
    def skills_insertion(self,skill):
        self.skills.append(skill)
p=Person("Ashutosh",22)
print(p.printing())
p.skills_insertion("Java")
print(p.printing())