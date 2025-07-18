class Student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def average(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hii",self.name,"your average sorce is:",sum/3)

s1=Student('Viral',[59,78,89])
# s1.average()
s1.name="ironman"               #this will override the name and use this one
s1.average()