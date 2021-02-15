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
    
        
class TestCircleCircumference(unittest.TestCase):
    
    def test_circlecircum_with_random_numeric_radius(self):
        # Define a circle 'c1' with radius 2.5, and check if 
        # its circumference is 15.71.
        c1 = Circle(2.5)
        self.assertEqual(c1.circumference(), 15.71)
       
    def test_circlecircum_with_min_radius(self):
        # Define a circle 'c2' with radius 0, and check if 
        # its circumference is 0.
        c1 = Circle(0)
        self.assertEqual(c2.circumference(), 0)

    def test_circlecircum_with_max_radius(self):
        # Define a circle 'c3' with radius 1000, and check if 
        # its circumference is 6283.19.
        c1 = Circle(1000)
        self.assertEqual(c1.circumference(), 6283.19)

