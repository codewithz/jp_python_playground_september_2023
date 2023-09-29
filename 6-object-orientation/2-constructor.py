class Point:

    def __init__(self,x,y):
        print("Point Constructor")
        self.x=x
        self.y=y

    def draw(self):
        print("Draw")
        print(f"Point ({self.x},{self.y})")

# -------------------------------------------------------

p=Point(10,20)
p.draw()
print(40*"-")


p1=Point(100,110)
p1.draw()

print(40*"-")

print(p)