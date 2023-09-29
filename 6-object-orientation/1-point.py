# functions and variables --< Snake Casing --> one_two_three_four
# Class--------------------> Pascal Casing --> OneTwoThreeFour


class Point:
    def draw(self):
        self.x=10
        self.y=20
        print("Draw")


# ---------------------------------------------------------

p=Point()
p.draw()
print("p.x:",p.x)
print("p.y:",p.y)
print(type(p))