import triangle
import vecteur


class Objet:
    def __init__(self, liste_de_triangle):
        self.triangles = [
            triangle.Triangle(vecteur.Vecteur(triangle_liste[0][0], triangle_liste[0][1], triangle_liste[0][2]),
                              vecteur.Vecteur(triangle_liste[1][0], triangle_liste[1][1], triangle_liste[1][2]),
                              vecteur.Vecteur(triangle_liste[2][0], triangle_liste[2][1], triangle_liste[2][2]))

            for triangle_liste in liste_de_triangle
        ]

    def toString(self):
        for TRIANGLE in self.triangles:
            TRIANGLE.to_string()
        print("Nb de triangles :", len(self.triangles))
