import math


class Vecteur:
    def __init__(self, x=0, y=0, z=0, w=1):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def toString(self):
        print("x : ", self.x)
        print("y : ", self.y)
        print("z : ", self.z)
        print("w : ", self.w)

def addVecteurNombre(vect, nombre):
    new_x = vect.x + nombre
    new_y = vect.y + nombre
    new_z = vect.z + nombre
    new_w = vect.w + nombre
    return Vecteur(new_x, new_y, new_z, new_w)

def multVecteurNombre(vect, nombre):
    new_x = vect.x * nombre
    new_y = vect.y * nombre
    new_z = vect.z * nombre
    new_w = vect.w * nombre
    return Vecteur(new_x, new_y, new_z, new_w)

def divVectNombre(vect, nombre):
    new_x = vect.x / nombre
    new_y = vect.y / nombre
    new_z = vect.z / nombre
    new_w = vect.w / nombre

def addVecteurVecteur(vect1, vect2):
    new_x = vect1.x + vect2.x
    new_y = vect1.y + vect2.y
    new_z = vect1.z + vect2.z
    new_w = vect1.w + vect2.w
    return Vecteur(new_x, new_y, new_z, new_w)

def  subVecteurVecteur(vect1, vect2):
    new_x = vect1.x - vect2.x
    new_y = vect1.y - vect2.y
    new_z = vect1.z - vect2.z
    new_w = vect1.w - vect2.w
    return Vecteur(new_x, new_y, new_z, new_w)

def dot(vect1, vect2):
    return vect1.x * vect2.x + vect1.y * vect2.y + vect1.z * vect2.z

def normalise(vect):
    taille = math.sqrt(dot(vect, vect))
    new_x = vect.x / taille
    new_y = vect.y / taille
    new_z = vect.z / taille
    return Vecteur(new_x, new_y, new_z)

def cross(vect1, vect2):
    new_x = vect1.y * vect2.z - vect1.z * vect2.y
    new_y = vect1.z * vect2.x - vect1.x * vect2.z
    new_z = vect1.x * vect2.y - vect1.y * vect2.x
    return Vecteur(new_x, new_y, new_z)