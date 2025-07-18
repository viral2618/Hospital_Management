#child/derived class that takes some methods and attributes parent/base 
# class which pass all the methods and attributest

#example for car company
class Car:
    _car_name="China"
    @staticmethod
    def start():
        print("car started ")
    @staticmethod
    def stop():
        print("Car stop")
class TATA(Car):
    def __init__(self,color,wheels):
        self.color=color
        self.wheels=wheels
    def TATA_CAr(self):
        print('car name exporter',self._car_name)
        print("car color",self.color)
        print("car wheels",self.wheels)

t1=TATA("blue",4)
t1.start()
t1.TATA_CAr()
t1.stop()


#multilevel inheritance
class Viral:
    name="viral"
class Abhishek(Viral):
    name2="abhishek"
class Harry(Abhishek):
    name3="harry"

h1=Harry()
print(h1.name)
print(h1.name2)
print(h1.name3)

# multiple inheritance
class viral:
    v1="viral"
class abhishek:
    v2="abhishek"
class harry(viral,abhishek):
    v3="harry"

h2=harry()
print(h2.v1)
print(h2.v2)
print(h2.v3)


# single inheritance
class Animal:
    def animal(self):
        print("some sound:")
class dog(Animal):
    def speak(self):
        print("dog bark")
d1=dog()
d1.animal()
d1.speak()


class Father:
    def skills(self):
        return ["Gardening", "Programming"]

class Mother:
    def skills(self):
        return ["Cooking", "Art"]

class Child(Mother,Father):
    pass

# Task: What is the output of Child().skills()?
c1=Child()
print(c1.skills())


# MRO - Method Resolution Order
class A:
    def show(self): print("A")

class B(A):
    def show(self): print("B")

class C(A):
    def show(self): print("C")

class D(B,C):
    pass

# Task: What will D().show() print? Why?
d1=D()
d1.show()

