class Student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @staticmethod
    def welcome():           #if you dot want to write self then you can use this ,
                                 # it will chage the behaviour it works at class level
        print("Welcome")
        
    def mark(self):
        return self.marks

s1=Student("viral",79)
s1.welcome()
print(s1.mark())