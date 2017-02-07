cdef extern from "func.h":
    int circle(int rad)
    int square(int side)

def circle_p(rad):
    area = circle(rad)
    if area == -1:
        raise RuntimeError()
    else:
        return area

def square_p(side):
    area = square(side)
    if area == -1:
        raise RuntimeError()
    else:
        return area
