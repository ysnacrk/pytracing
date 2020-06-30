from shape import *

def write_color(camera : Vec3 , rd : Vec3, shapes) -> None:
    intersect_list = []
    intersect = Intersect(0 , 0)

    for i in range(0 , 3):
        t = shapes[i].intersect(camera  , rd)
        
        if t > 0.0:
            intersect.distance = t
            intersect.indice   = i
            
            intersect_list.append(intersect)
    
    if len(intersect_list) > 0:
        min_distance = 3.402823466e+38     
        min_indis    = -1

        for i in range(len(intersect_list)):
            if intersect_list[i].distance < min_distance:
                min_indis = intersect_list[i].indice
                min_distance = intersect_list[i].distance

        return shapes[min_indis].color

    return Color(0, 0 ,0)     


def main() -> None:

    print("P3\n" + str(800) + " " + str(450) + "\n255\n")

    t1 = Triangle(Vec3(0, 30,  40), Vec3(40, -30, 120), Vec3(-40, -30, 120) ,Color(255 , 0 , 0))
    t2 = Triangle(Vec3(-50, 30,  124), Vec3(50, 30, 124), Vec3(0, -30, 44) ,Color(0 , 255 , 0))
    t3 = Triangle(Vec3(-30, 0,  37), Vec3(30, 40, 117), Vec3(30, -40, 117) ,Color(0 , 0 , 255))

    shapes = (t1, t2, t3)
    camera = Vec3(0, 0, 0)

    for j in range(0, 450):
        for i in range(0, 800):
            pixel = Vec3(16 * i / 799.0 - 8 , 4.5 - j * 9 / 449.0 , 10)
            rd = (pixel - camera).normalize
            color = write_color(camera, rd, shapes)
            print(str(color.r) + " " + str(color.g) + " " + str(color.b))

if __name__ == "__main__":
    main()
