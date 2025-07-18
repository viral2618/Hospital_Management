class Book:
    def __init__(self,name,author):
        self.name=name
        self.author=author

class EBook(Book):
    def __init__(self, name, author,file_size):
        self.file_size=file_size
        super().__init__(name, author)
    def print_method(self):
        print(f"Book name is {self.name} and the author is {self.author} file size is {self.file_size}")
        
e1=EBook("haunted adeline","viral",344)
e1.print_method()


class Vehicle:
    def start_engine(self):
        print("engine starts")

class Truck(Vehicle):
    def load_goods(self):
        print('goods are loaded')
t1=Truck()
t1.start_engine()
t1.load_goods()



