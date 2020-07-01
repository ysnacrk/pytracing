from vec3 import *
from color import *
from math import *


class Shape: 
    def __init__(self, color : Color) -> None:
        self.color = color

   
        

class Triangle(Shape):
    
    def __init__(self, v0: Vec3, v1: Vec3, v2: Vec3 , color) -> None:
        self.v = (v0, v1, v2)
        self.color = color

    

    def intersect(self , r: Vec3 , direction: Vec3):

        #ışının bu üçgenin bulunduğu yüzeyden geçip geçmediğini kontrol ediyoruz
        # eğer o yüzey ile kesişiyorsa üçgeninin içinde mi onu kontrol ediyoruz

        normal = (self.v[1] - self.v[0]).crossProduct(self.v[2] - self.v[1])
        D = - (dot(normal  , self.v[0]))
        t = -(dot(normal , r ) + D) / dot(normal , direction)

        if t>0:
            intersectPoint = r + t * direction

            S = (self.v[1] - self.v[0]).crossProduct(self.v[2] - self.v[1]).length

            s1 = ( intersectPoint - self.v[0]).crossProduct(self.v[2] -  intersectPoint).length
            s2 = (self.v[1] - self.v[0]).crossProduct(intersectPoint - self.v[1]).length
            s3 = (self.v[1] -  intersectPoint).crossProduct(self.v[2]- self.v[1]).length

            diff = abs(S - (s1 + s2 + s3))
            epsilon = 0.005

            if diff <= epsilon:
                return t
            else:
                return 0
        else :
            return 0

class Sphere(Shape):

    def __init__(self, center : Vec3 , radius : float, color : Color) -> None:
        self.center = center
        self.color = color
        self.radius = radius


    def intersect(self, r, direction):
        l = self.center - r 
        s = dot(l , direction)
        l2 = dot(l, l)
        r2 = self.radius * self.radius

        if s < 0 and l2 > r2:
            return 0
        
        s2 = s * s
        m2 = l2 - s2

        if m2 > r2:
            return 0

        q = sqrt(r2 - m2)

        if l2 > r2:
            return s - q
        else:
            return s + q

class Intersect:
    def __init__(self,indice, distance):
        self.indice = indice
        self.distance = distance




    
