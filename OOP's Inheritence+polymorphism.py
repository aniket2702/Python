#Aniket Sharma
#G-704

#Assignment 11(c)
#main Class
class Bird:
    def intro(self):
        print("There are different types of birds")

    def flight(self):
        print("Most of the birds can fly but some cannot")
#inherited class with polymorphism
class pigeon(Bird):
    def flight(self):
        print("Pigeon can fly")
#inherited class with polymorphism
class penguin(Bird):
    def flight(self):
        print("Penguins do not fly")
#inherited class with polymorphism
class kingfisher(Bird):
    def flight(self):
        print("Kingfisher can fly")
#creating object of each class
bird = Bird()
pige = pigeon()
peng = penguin()
king = kingfisher()
#calling functions of different classes
bird.intro()
bird.flight()
print("\n")
pige.intro()
pige.flight()

peng.intro()
peng.flight()

king.intro()
king.flight()