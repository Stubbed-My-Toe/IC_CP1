#IC CP2 geometry calc: shape maker

class Circle:
        def __init__(self, radius, area, perimeter, diameter):
                self.radius = radius
                self.area = area
                self.perimeter = perimeter
                self.diameter = diameter


def create_circle(Circle):
       circle_radius = float("What do you want the radius of your circle to be?")
       Circle"circle"


print("""=====================================
    CREATE NEW SHAPE
    =====================================""")

def what_shape(picked_shape):
    picked_shape = ("""Available Shapes:

        [1] Circle
        [2] Rectangle
        [3] Square
        [4] Triangle

        Enter shape type (1-4): """).strip()
    return
what_shape()

if picked_shape == "1":
        pass
elif picked_shape == "2":
        pass
elif picked_shape == "3":
        pass
elif picked_shape == "4":
        pass
else:
        what_shape()