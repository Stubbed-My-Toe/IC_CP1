#IC Classes Notes

#example 1
class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def __str__(self):
        return f"""Name: {self.name}\nspecies: {self.species}\nage: {self.age} """
    
    def unc(self):
        self.age += 1


dog = Animal('Doug', 'dog', 4)
bunny = Animal("Judy", "rabbit", 500)
print(dog)
print(bunny)
dog.unc()
print(dog)

#EXAMPLE 2
class ClassPeriod:
    def __init__(self, subject, teacher = "The Big Mac", room = None):
        self.subject = subject.capitalize()
        self.teacher = teacher
        self.room = room

    def __str__(self):
        return f"Subject: {self.subject}\nTeacher: {self.teacher}\nRoom: {self.room}\n"
    
first = ClassPeriod("Boston Sim", room = "i forgot")

print(first)
