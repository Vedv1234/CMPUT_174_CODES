# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my implementation of a Circle class where I'm learning
# about object-oriented programming. I've created methods to calculate area and perimeter,
# and I'm practicing with special methods like __init__ and __str__.

class Circle:
    def __init__(self, radius_p1):
        # This is my constructor where I set up a new circle
        # I'm learning that self is like 'this' in Java - it refers to the current object
        # I'm storing the radius as a property of my circle
        self.radius = radius_p1

    def __str__(self):
        # I created this special method to give my circle a nice string representation
        # when it's printed
        return f'I am a Circle of radius {self.radius}'
    
    def get_perimeter(self):
        # My method to calculate the circle's perimeter using the formula 2πr
        return 2 * 3.142 * self.radius

    def get_area(self):
        # My method to calculate the circle's area using the formula πr²
        return 3.142 * self.radius ** 2
        
def main():
    # This is where I test my Circle class
    c1 = Circle(5)  # I'm creating my first circle with radius 5
    # When I create a circle:
    # 1. A new circle object is created
    # 2. The __init__ method is called to set it up
    
    # Testing my area and perimeter calculations
    area_c1 = c1.get_area()
    perimeter_c1 = c1.get_perimeter()
    print(f" Circle C1 Area : {area_c1} Perimeter : {perimeter_c1}")
    
    # Creating more circles to test my class
    c2 = Circle(7)
    c3 = Circle(8)
    # Testing my __str__ method with different circles
    print(c1)
    print(c2)
    print(c3)

main()