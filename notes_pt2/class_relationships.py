#IC CP2 Class Relationship Notes

#parent class
class Vehical:
    def __init__(self, model, brand):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move")

#Child Class
class Car(Vehical):
    pass

class Butt(Vehical):
    def move(self):
        print("Sail")


class Plane(Vehical):
    def move(self):
        print("Fly")

car = Car("Toyota", "1984 Hilux")
boat = Butt("MasterCraft", "X-45")
plane = Plane("Fairchild", "A-10 Warthog")

print(car.brand)
print(car.model)
car.move()
boat.move()
plane.move()


#aggregation 'has a'
class Library:
    def __init__(self, name, catalog = []):
        self.name = name
        self.catalog = catalog

    def add_book(self, book):
        self.catalog.append(book)

    def remove_book(self, book):
        if book in self.catalog:
            self.catalog.pop(book)
        else:
            print("YO YO! THAT BOOK AIN'T IN THE LIBRARY FOOL")

    def view_catalog(self):
        for book in self.catalog:
            print(book)

class Book:
    def __init__(self, title, author):
        self.title = title.title()
        self.author = author
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    

lib = Library("Provo Library")
lib.add_book(Book("How to Become Goated at Fortnite", "Jonesy"))
lib.add_book(Book("Fablehaven", "Brandon Sanderson"))
lib.add_book(Book("Encyclopedia of Evil Slugs", "Handbag"))

lib.view_catalog()