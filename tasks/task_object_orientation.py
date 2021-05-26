import math

class Shape:
    def __init__(self, a=10, b=6):
        self.set_params(a, b)

    def set_params(self, a, par_b):
        self.a = a
        self.b = par_b

    def get_a(self):
        return self.a

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self.a) + " by " + str(self.b) + "] at " + str(hex(id(self)))


class Rectangle(Shape):
    def calc_surface(self):
        return self.a*self.b

    def swap_sides(self):
        a = self.a
        b = self.b
        self.a = b
        self.b = a

    def perimeter(self):
        return 2*self.a + 2*self.b

class Circle(Shape):
    def __init__(self, a):
        # call constructor of superclass (parent)
        super().__init__(a, 0)
        #self._a = a

    def calc_surface(self):
        return math.pi * self.a**2

    def __repr__(self):
        return self.__class__.__name__ + "[r=" + str(self.a) + "] at " + str(hex(id(self)))

    def perimeter(self):
        return 2*math.pi * self.a


class Sphere(Circle):
    def calc_volume(self):
        return 4/3*math.pi*self.a**3

    def calc_surface(self):
        return 4*super().calc_surface()


#new class: Triangle

class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c=c

    def calc_surface(self):
        s = 1/2 * (self.a + self.b + self.c)
        return math.sqrt(s(s-self.a)(s-self.b)(s-self.c))

    def perimeter(self):
        return self.a + self.b + self.c


#new class: Equilateral Triangle

class EquilateralTriangle(Triangle):
    def __init__(self, a):
        super().__init__(a, 0, 0)

    def calc_surface(self):
        return math.sqrt(3)*self.a/4

    def perimeter(self):
        return 3*self.a


#new class: Square (inherits from Rectangle)

class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)

#new examples (deleted existing)

print('-----Rectangle-----')
r = Rectangle(2,3)
print(r)
print(r.perimeter())
print(r.perimeter() == 2*2+2*3)

r2 = Rectangle(2,5)
print(r2)
print(r2.perimeter())
print(r2.perimeter() == 2*2+2*3) #should be false

print('-----Circle-----')
c = Circle(5)
print(c)
print(c.perimeter())
print(c.perimeter() == (2*math.pi*5))

print('-----Triangle-----')
t = Triangle(1,2,3)
#t_false = Triangle(1,2) - gives error as expected when running it, as c is missing
print(t)
print(t.perimeter())
print(t.perimeter() == 1+2+3)

t2 = Triangle(1,2,5)
print(t2)
print(t2.perimeter())
print(t2.perimeter() == 1+2+3) #should be false

print('-----EquilateralTriangle-----')
et = EquilateralTriangle(3)
#et_false = EquilateralTriangle(2,3,4) #gives error as expected when running because too many are given
print(et)
print(et.perimeter())
print(et.perimeter() == 3*3)

print('-----Square-----')
sq = Square(5)
print(sq)
print(sq.calc_surface())
print(sq.calc_surface() == 5*5)
print(sq.perimeter())
print(sq.perimeter() == 4*5)


