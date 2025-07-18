class Viral:
    college_name='nirmala'      #class attributes
    name="anonymous"
    def __init__(self, name, marks):
        self.name = name    #instance/object attributes haar ek object ke liyee aalag hogee
        self.marks = marks     #self is object reference and it is used to get the value
    
v=Viral("viral",99)
print(v.name,v.marks,v.college_name)    #all the new object will occupy space in the memory

v2=Viral("abhishek", 100)
print(v2.name, v2.marks, v2.college_name)   #you can also access the class sttribute
                                                #by using class name.attribute
                                                
                                                #object attr> class attributes zada 
                                                # prior hote hai obj
