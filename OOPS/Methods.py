class Student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def welcome(self):
        print("Welcome,",self.name)
        
    def mark(self):
        return self.marks

s1=Student("viral",79)
s1.welcome()
print(s1.mark())