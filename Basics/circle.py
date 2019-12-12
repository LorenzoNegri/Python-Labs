"""circle module: contains the Circle Class."""
class Circle:
    """Circle Class"""
    all_circles = [] # class variable containg a list of all circles created
    pi = 3.14159
    def __init__(self, r=1):
        """Create a Circle with the given radius"""
        self.radius = r
        self.__class__.all_circles.append(self) # when an instance is being initialized this adds to all_circles list
    def area(self):
        """determine the area of the Circle"""
        return self.__class__.pi * self.radius * self.radius
    
    @staticmethod
    def total_area():
        """Static method to total the areas of all Circles"""
        total = 0
        for c in Circle.all_circles:
            total = total + c.area()
        return total
