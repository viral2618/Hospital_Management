class Device:
    def __init__(self,name):
        self.name=name
        print('device initialized')
    
class Mobile(Device):
    def M_working(self):
        print(f"We also sell the same {self.name} brand phone")
        
class Laptop(Device):
    def L_usage(self):
        print(f"Most of the company uses {self.name} laptop")
        
class SmartGadget(Mobile,Laptop):
    def __init__(self, name):
        super().__init__(name)
    def AI(self):
        print(f"Both uses Ai powered systems")

s1=SmartGadget("Lenovo")
