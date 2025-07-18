class Appliance:
    def __init__(self,name):
        self.name=name
class washingMachine(Appliance):
    def manual(self):
        print(f"washing machine works manual without ai\ncompany name {self.name}")
class smartWasher(washingMachine):
    def automatic(self):
        print(f"smartwasher works automatically with ai\ncompany name {self.name}")

s1=smartWasher("Godrej")
s1.manual()
s1.automatic()