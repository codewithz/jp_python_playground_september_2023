class Animal:
    def eat(self):
        print("Eat")

# ----------------------------------------------------

# Animal -- Parent or Base Class

# Mammal , Fish -- Child or Derived Class
#     class Child(Parent):

      # class Mammal(Animal):

# ------------------------------------------------

class Mammal(Animal):
    def walk(self):
        print("Walk")

# ----------------------------------------

class Fish(Animal):
    def swim(self):
        print("Swim")

# ---------------------------------------------

m=Mammal()
m.eat()
m.walk()

f=Fish()
f.eat()
f.swim()