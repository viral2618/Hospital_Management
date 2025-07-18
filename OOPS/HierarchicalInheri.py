class Fruit:
    def nutrition(self):
        print("fruits has good nutrition")
    
class Apple(Fruit):
    def taste(self):
        print("it tastes sweet apple")
        
class banana(Fruit):
    def taste(self):
        print("it tastes sweet banana")

b1=banana()
b1.taste()