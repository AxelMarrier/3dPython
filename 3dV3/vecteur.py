import math


class Vecteur:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def to_list(self):
        return [self.x, self.y, self.z]

    def copy(self):
        return Vecteur(self.x, self.y, self.z)

    def to_string(self):
        print([self.x, self.y, self.z])

    def rotate_x(self, rotation):
        cos_r = math.cos(rotation)
        sin_r = math.sin(rotation)

        original_y = self.y
        original_z = self.z

        self.y = original_y * cos_r - original_z * sin_r
        self.z = original_y * sin_r + original_z * cos_r

    def rotate_y(self, rotation):
        cos_r = math.cos(rotation)
        sin_r = math.sin(rotation)

        original_x = self.x
        original_z = self.z

        self.x = original_x * cos_r + original_z * sin_r
        self.z = -original_x * sin_r + original_z * cos_r

    def rotate_z(self, rotation):
        cos_r = math.cos(rotation)
        sin_r = math.sin(rotation)

        original_x = self.x
        original_y = self.y

        self.x = original_x * cos_r - original_y * sin_r
        self.y = original_x * sin_r + original_y * cos_r


""" ADDITION """


def add_vect_int(vect, nombre):
    return Vecteur(vect.x + nombre, vect.y + nombre, vect.z + nombre)


def add_vect_vect(vect1, vect2):
    return Vecteur(vect1.x + vect2.x, vect1.y + vect2.y, vect1.z + vect2.z)


""" SOUSTRACTION """


def sub_vect_int(vect, nombre):
    return Vecteur(vect.x - nombre, vect.y - nombre, vect.z - nombre)


def sub_vect_vect(vect1, vect2):
    return Vecteur(vect1.x - vect2.x, vect1.y - vect2.y, vect1.z - vect2.z)


""" MULTIPLICATION """


def mult_vect_int(vect, nombre):
    return Vecteur(vect.x * nombre, vect.y * nombre, vect.z * nombre)


def mult_vect_vect(vect1, vect2):
    return Vecteur(vect1.x * vect2.x, vect1.y * vect2.y, vect1.z * vect2.z)


""" DIVISION """


def div_vect_int(vect, membre):
    return Vecteur(vect.x / membre, vect.y / membre, vect.z / membre)


def div_vect_vect(vect1, vect2):
    return Vecteur(vect1.x / vect2.x, vect1.y / vect2.y, vect1.z / vect2.z)


def cross_product(vect1, vect2):
    x = vect1.y * vect2.z - vect1.z * vect2.y
    y = vect1.z * vect2.x - vect1.x * vect2.z
    z = vect1.x * vect2.y - vect1.y * vect2.x
    return Vecteur(x, y, z)


def dot_product(vect1, vect2):
    return vect1.x * vect2.x + vect1.y * vect2.y + vect1.z * vect2.z

def normaliser(vect):
    ampleur = math.sqrt(vect.x ** 2 + vect.y ** 2 + vect.z ** 2)
    if ampleur != 0:
        return div_vect_int(vect, ampleur)
    else:
        return vect
