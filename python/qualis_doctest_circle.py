# Unit Testing using doctest in Python
#Circle

import inspect
import doctest
import re
import math

# Define the class 'Circle' and its methods with proper doctests:
class Circle:
    
    def __init__(self, radius):
        # Define doctests for __init__ method:
        """
        >>> c1 = Circle(2.5)
        >>> c1.radius
        2.5
        """
        self.radius = radius

        
    def area(self):
        # Define doctests for area method:
        """
        >>> c1 = Circle(2.5)
        >>> c1.area() 
        19.63
        """
        # Define area functionality:
        return round(((self.radius ** 2) * math.pi),2)        
        

    def circumference(self):
        # Define doctests for circumference method:
        """
        >>> c1 = Circle(2.5)
        >>> c1.circumference()
        15.71
        """
        # Define circumference functionality:
        return round((2 * math.pi * self.radius),2)