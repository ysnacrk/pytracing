



from color import write_color
from vec3 import *
from ray import *


def ray_color(ray : Ray):

    unit_direction = unit_vector(ray.direction)
    t = 0.5*(unit_direction.y + 1.0)
    return (1.0-t)*Vec3(1.0, 1.0, 1.0) + t*Vec3(0.5, 0.7, 1.0)
    
aspect_ratio = 16.0 / 9.0

img_width = 384
img_height = int(img_width / aspect_ratio)

viewport_height = 2.0
viewport_width = aspect_ratio * viewport_height
focal_length = 1.0

horizantal = Point3(viewport_width , 0 , 0)
vertical = Point3(0 , viewport_height ,0)
origin = Point3(0 , 0 , 0)

lower_left_corner = origin - horizantal / 2 - vertical / 2 - Vec3(0, 0, focal_length)

print("P3\n" + str(img_width) + " " + str(img_height) + "\n255")

for j in range(img_height, 0 , -1):
    for i in range(0, img_width):
        u = i / (img_width - 1)
        v = j / (img_height - 1)
        r = Ray(origin , lower_left_corner + u*horizantal + v*vertical - origin)
        pixel_color = ray_color(r)
        write_color(pixel_color)

