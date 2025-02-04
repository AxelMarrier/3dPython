import math
import vecteur


class Triangle:

    def __init__(self, origine, vect1, vect2):
        self.origine = origine
        self.vect1 = vect1
        self.vect2 = vect2
        self.orientation = self.setOrientation()
        self.avg_z = self.setAvgZ()

    def copy(self):
        new_triangle = Triangle(
            self.origine.copy(),  # Create a copy of the origine list
            self.vect1.copy(),  # Create a copy of the vect1 list
            self.vect2.copy()  # Create a copy of the vect2 list
        )
        return new_triangle

    def to_string(self):
        print("Point d'origine du triangle ", self.origine.x, self.origine.y, self.origine.z)
        print("Point 1 du triangle", self.vect1.x, self.vect1.y, self.vect1.z)
        print("Point 2 du triangle", self.vect2.x, self.vect2.y, self.vect2.z)
        print("Orientation : ", self.orientation.x, self.orientation.y, self.orientation.z)

    def setAvgZ(self):
        return (self.origine.z + self.vect1.z + self.vect2.z) / 3

    def setOrientation(self):
        cross1 = vecteur.sub_vect_vect(self.vect1, self.origine)

        cross2 = vecteur.sub_vect_vect(self.vect2, self.origine)

        crossProduct = vecteur.cross_product(cross1, cross2)

        crossProductNormaliser = vecteur.normaliser(crossProduct)

        return crossProductNormaliser

    def setOrigine(self, new_point):
        self.origine = new_point

    def setVect1(self, new_point):
        self.vect1 = new_point

    def setVect2(self, new_point):
        self.vect2 = new_point

    def reverse(self):
        point = self.vect1
        self.setVect1(self.vect2)
        self.setVect2(point)
        self.setOrientation()

    def rotateZ(self, rotation):

        # Origine
        self.origine.rotate_z(rotation)

        # Point 1
        self.vect1.rotate_z(rotation)

        # Point 2
        self.vect2.rotate_z(rotation)

    def rotateY(self, rotation):

        # Origine
        self.origine.rotate_y(rotation)

        # Point 1
        self.vect1.rotate_y(rotation)

        # Point 2
        self.vect2.rotate_y(rotation)

    def rotateX(self, rotation):

        # Origine
        self.origine.rotate_x(rotation)

        # Point 1
        self.vect1.rotate_x(rotation)

        # Point 2
        self.vect2.rotate_x(rotation)

    def camera_transform(self, matrice):
        new_x = self.origine.x * matrice[0][0] + self.origine.y * matrice[1][0] + self.origine.z * matrice[2][0] + matrice[3][0]
        new_y = self.origine.x * matrice[0][1] + self.origine.y * matrice[1][1] + self.origine.z * matrice[2][1] + matrice[3][1]
        new_z = self.origine.x * matrice[0][2] + self.origine.y * matrice[1][2] + self.origine.z * matrice[2][2] + matrice[3][2]
        new_origine = vecteur.Vecteur(new_x, new_y, new_z)

        new_x = self.vect1.x * matrice[0][0] + self.vect1.y * matrice[1][0] + self.vect1.z * matrice[2][0] + matrice[3][0]
        new_y = self.vect1.x * matrice[0][1] + self.vect1.y * matrice[1][1] + self.vect1.z * matrice[2][1] + matrice[3][1]
        new_z = self.vect1.x * matrice[0][2] + self.vect1.y * matrice[1][2] + self.vect1.z * matrice[2][2] + matrice[3][2]
        new_vect1 = vecteur.Vecteur(new_x, new_y, new_z)

        new_x = self.vect2.x * matrice[0][0] + self.vect2.y * matrice[1][0] + self.vect2.z * matrice[2][0] + matrice[3][0]
        new_y = self.vect2.x * matrice[0][1] + self.vect2.y * matrice[1][1] + self.vect2.z * matrice[2][1] + matrice[3][1]
        new_z = self.vect2.x * matrice[0][2] + self.vect2.y * matrice[1][2] + self.vect2.z * matrice[2][2] + matrice[3][2]
        new_vect2 = vecteur.Vecteur(new_x, new_y, new_z)

        return Triangle(new_origine, new_vect1, new_vect2)