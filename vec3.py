

class Vec3: 

    def __init__(self, e0: float, e1: float, e2: float) -> None:
        self.e = (e0, e1, e2)

    def __neg__(self):
        return Vec3(-self.e[0], -self.e[1], -self.e[2]))
    
    def __add__(self, other):
        return Vec3(self.e[0] + other.e[0] , self.e[1] + other.e[1] ,self.e[2] + other.e[2])
    
    def __sub__(self, other):
        return Vec3(self.e[0] - other.e[0] , self.e[1] - other.e[1] ,self.e[2] - other.e[2])
    

    def __mul__(self, other: typing.Union["Vec3", float]):
        if isinstance(other, (float, int)):
            o = (other, other, other)
        else:
            o = other.e
        return Vec3(self.e[0] * o[0], self.e[1] * o[1], self.e[2] * o[2])
    
    def __rmul__(self, other: typing.Union["Vec3", float]) -> "Vec3":
        return self.__mul__(other)
    
    def __truediv__(self, other: typing.Union["Vec3", float, int]):
        if isinstance(other, (float, int)):
            o = (other, other, other)
        else:
            o = other.e
        return Vec3(self.e[0] / o[0], self.e[1] / o[1], self.e[2] / o[2])

    def __isub__(self, other):
        return Vec3(self.e[0]-other.e[0], self.e[1]-other.e[1] , self.e[2]-other.e[2])
    
    def __iadd__(self, other):
        return Vec3(self.e[0]+other.e[0], self.e[1]+other.e[1] , self.e[2]+other.e[2])
    
    def __imul__(self, other):
        return Vec3(self.e[0]*other , self.e[1]*other , self.e[2]*other)
    
    def __itruediv__(self, other):
        return Vec3(self.e[0]/other , self.e[1]/other , self.e[2]/other)

    def __str__(self):
            return self.x + " " + self.y + " " +  self.z 


    @property
    def length(self):
        return sqrt(self.e[0] * self.e[0] + self.e[1]*self.e[1] + self.e[2]*self.e[2])
    @property
    def x(self):
        return self.e[0]

    @property
    def y(self):
        return self.e[1]

    @property
    def z(self):
        return self.e[2]

def dot(u: Vec3, v: Vec3) -> float:
    return u.e[0] * v.e[0] + u.e[1] * v.e[1] + u.e[2] + v.e[2]

def unit_vector(v: Vec3) -> Vec3:  
    return v / v.length

def cross(u: Vec3, v: Vec3) -> Vec3:  # TODO: inline function
    return Vec3(
        u.e[1] * v.e[2] - u.e[2] * v.e[1],
        u.e[2] * v.e[0] - u.e[0] * v.e[2],
        u.e[0] * v.e[1] - u.e[1] * v.e[0],
    )


class Point3(Vec3):
    pass

class Color(Vec3):
    pass