import math

class Triangle:

    def __init__(self, origine, point1, point2):
        self.origine = origine
        self.point1 = point1
        self.point2 = point2
        self.orientation = self.setOrientation()
        self.avgZ = (origine[2] + point1[2] + point2[2]) / 3

    def copy(self):
        new_triangle = Triangle(
            self.origine.copy(),  # Create a copy of the origine list
            self.point1.copy(),  # Create a copy of the point1 list
            self.point2.copy()  # Create a copy of the point2 list
        )
        return new_triangle
    def toString(self):
        print("Point d'origine du triangle ", self.origine)
        print("Point 1 du triangle", self.point1)
        print("Point 2 du triangle", self.point2)

    def setAvgZ(self):
        self.avgZ = (self.origine[2] + self.point1[2] + self.point2[2]) / 3

    def setOrientation(self):

        x1, y1, z1 = self.point1
        x2, y2, z2 = self.point2
        xo, yo, zo = self.origine

        v1x, v1y, v1z = x1 - xo, y1 - yo, z1 - zo
        v2x, v2y, v2z = x2 - xo, y2 - yo, z2 - zo

        nx = v1y * v2z - v1z * v2y
        ny = v1z * v2x - v1x * v2z
        nz = v1x * v2y - v1y * v2x

        magnitude = math.sqrt(nx ** 2 + ny ** 2 + nz ** 2)

        if magnitude != 0:
            nx /= magnitude
            ny /= magnitude
            nz /= magnitude
        self.orientation = [nx,ny,nz]
        return [nx,ny,nz]

    def setOrigine(self, newPoint):
        self.origine = newPoint

    def setPoint1(self,newPoint):
        self.point1 = newPoint

    def setPoint2(self, newPoint):
        self.point2 = newPoint

    def reverse(self):
        point = self.point1
        self.setPoint1(self.point2)
        self.setPoint2(point)
        self.setOrientation()

    def rotateZ(self, rotation):
        cos_r = math.cos(rotation)
        sin_r = math.sin(rotation)

        # Origine
        x = self.origine[0] * cos_r - self.origine[1] * sin_r
        y = self.origine[0] * sin_r + self.origine[1] * cos_r
        self.origine[0] = x
        self.origine[1] = y

        # Point 1
        x = self.point1[0] * cos_r - self.point1[1] * sin_r
        y = self.point1[0] * sin_r + self.point1[1] * cos_r
        self.point1[0] = x
        self.point1[1] = y

        # Point 2
        x = self.point2[0] * cos_r - self.point2[1] * sin_r
        y = self.point2[0] * sin_r + self.point2[1] * cos_r
        self.point2[0] = x
        self.point2[1] = y

    def rotateX(self, rotation):
        cos_r = math.cos(rotation)
        sin_r = math.sin(rotation)

        # Origine
        y = self.origine[1] * cos_r - self.origine[2] * sin_r
        z = self.origine[1] * sin_r + self.origine[2] * cos_r
        self.origine[1] = y
        self.origine[2] = z

        # Point 1
        y = self.point1[1] * cos_r - self.point1[2] * sin_r
        z = self.point1[1] * sin_r + self.point1[2] * cos_r
        self.point1[1] = y
        self.point1[2] = z

        # Point 2
        y = self.point2[1] * cos_r - self.point2[2] * sin_r
        z = self.point2[1] * sin_r + self.point2[2] * cos_r
        self.point2[1] = y
        self.point2[2] = z

    def rotateY(self, rotation):
        cos_r = math.cos(rotation)
        sin_r = math.sin(rotation)

        # Origine
        x = self.origine[0] * cos_r + self.origine[2] * sin_r
        z = -self.origine[0] * sin_r + self.origine[2] * cos_r
        self.origine[0] = x
        self.origine[2] = z

        # Point 1
        x = self.point1[0] * cos_r + self.point1[2] * sin_r
        z = -self.point1[0] * sin_r + self.point1[2] * cos_r
        self.point1[0] = x
        self.point1[2] = z

        # Point 2
        x = self.point2[0] * cos_r + self.point2[2] * sin_r
        z = -self.point2[0] * sin_r + self.point2[2] * cos_r
        self.point2[0] = x
        self.point2[2] = z