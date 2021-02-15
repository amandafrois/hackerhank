# Unit testing of a class using Nose
# Circle


def test_creating_circle_with_numeric_radius(self):
 
    c1 = Circle(2.5)
    self.assert_equal(c1.radius, 2.5)
 
 
def test_creating_circle_with_negative_radius(self):
 
    c1 = Circle(2.5)
    self.assert_equal(c1.radius, 2.5)
    self.assert_raises(ValueError, Circle, -2.5)
 
 
def test_creating_circle_with_greaterthan_radius(self):
 
    c1 = Circle(2.5)
    self.assert_equal(c1.radius, 2.5)
    self.assert_raises(ValueError, Circle, 1000.1)
 
 
def test_creating_circle_with_nonnumeric_radius(self):
 
    c1 = Circle(2.5)
    self.assert_equal(c1.radius, 2.5)
    self.assert_raises(TypeError, Circle, "hello")


from proj.circle import Circle
from nose.tools import assert_raises
 
class TestingCircleCreation:
    def test_creating_circle_with_numeric_radius(self):
        c1 = Circle(2.5)
        assert c1.radius == 2.5
 
    def test_creating_circle_with_negative_radius(self):
        with assert_raises(ValueError) as e:
            c = Circle(-2.5)
        assert str(e.exception) == "radius must be between 0 and 1000 inclusive"
 
    def test_creating_circle_with_greaterthan_radius(self):
        with assert_raises(ValueError) as e:
            c = Circle(1000.1)
        assert str(e.exception) == "radius must be between 0 and 1000 inclusive"
 
    def test_creating_circle_with_nonnumeric_radius(self):
        with assert_raises(TypeError) as e:
            c = Circle("hello")
        assert str(e.exception) == "radius must be a number"
 
 
class TestCircleArea:
    def test_circlearea_with_random_numeric_radius(self):
        c1 = Circle(2.5)
        assert c1.area() == 19.63
 
    def test_circlearea_with_min_radius(self):
        # Define a circle 'c2' with radius 0, and check if
        # its area is 0.
        c2 = Circle(0)
        assert c2.area() == 0
 
    def test_circlearea_with_max_radius(self):
        c3 = Circle(1000)
        assert c3.area() == 3141592.65
 
 
class TestCircleCircumference:
    def test_circlecircum_with_random_numeric_radius(self):
        c1 = Circle(2.5)
        assert c1.circumference() == 15.71
 
    def test_circlecircum_with_min_radius(self):
        c2 = Circle(0)
        assert c2.circumference() == 0
 
    def test_circlecircum_with_max_radius(self):
        c3 = Circle(1000)
        assert c3.circumference() == 6283.19
