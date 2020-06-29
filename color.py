
import vec3

def write_color(color:vec3) -> None:
    r = int(color.x * 255.999)
    g = int(color.y * 255.999)
    b = int(color.z * 255.999)

    print("{} {} {}".format(r, g, b))