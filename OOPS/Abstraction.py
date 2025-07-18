from abc import ABC,abstractmethod
class Animal(ABC):
    def __init__(self,sound):
        self.sound=sound
    @abstractmethod
    def make_sound(self):
        pass
class Cat(Animal):
    def make_sound(self):
        print(self.sound)
        
class dog(Animal):
    def make_sound(self):
        print(self.sound)

class fish(Animal):
    def make_sound(self):
        print(self.sound)
        
c1=Cat('MEOW!')
c1.make_sound()
d1=dog("WOOF!")
d1.make_sound()
f1=fish("WEEEEEEE!")
f1.make_sound()