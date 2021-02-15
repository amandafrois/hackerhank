# Unit Testing using unittest in Python
# Circle

class Circle:
    
    def __init__(self, radius): 
        # Define initialization method: 
        self.radius=radius 
        if not isinstance(self.radius,(int,float)): 
            raise TypeError("radius must be a number") 
        elif(self.radius >1000 or self.radius <0): 
            raise ValueError("radius must be between 0 and 1000 inclusive") 
        else: 
            pass 
 
    def area(self): 
        # Define area functionality: 
        return round(math.pi*(self.radius**2),2) 
 
    def circumference(self): 
        # Define circumference functionality: 
        return round(2*math.pi*self.radius,2)
   
        
class TestCircleArea(unittest.TestCase):
    
    def test_circlearea_with_random_numeric_radius(self):
        # Define a circle 'c1' with radius 2.5, and check if 
        # its area is 19.63.
        c1 = Circle(2.5)
        self.assertEqual(c1.area(),19.63)
        
    def test_circlearea_with_min_radius(self):
        # Define a circle 'c2' with radius 0, and check if 
        # its area is 0.
        c2 = Circle(0.0)
        self.assertEqual(c2.area(),0)
        
    def test_circlearea_with_max_radius(self):
        # Define a circle 'c3' with radius 1000.1. and check if 
        # its area is 3141592.65.
        with self.assertRaises(ValueError) as e:
            c3 = Circle(1000.1)
        self.assertEqual(str(e.exception), "radius must be between 0 and 1000 inclusive")
