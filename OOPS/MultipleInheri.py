class Gps:
    def __init__(self,map,direction):
        self.map=map
        self.direction=direction

class Camera:
    def __init__(self,click,picture):
        self.click=click
        self.picture=picture

class Smartcar(Gps,Camera):
    def __init__(self, map, direction,click,picture):
        Gps.__init__(self,map, direction)
        Camera.__init__(self,click,picture)
    def auto_driver(self):
        print(f"this smart car has {self.map} we are going in {self.direction} {self.click} {self.picture}")

s1 = Smartcar("Google Maps", "North", "High-res click", "HD Picture")
s1.auto_driver()