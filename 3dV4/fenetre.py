import tkinter as tk
import math
import vecteur


class Fenetre:

    def __init__(self, nom="fenetre", width=800, height=600, fov=90, z_max=1000, z_min=0.1, color="green"):
        self.width = width
        self.height = height
        self.fov = math.radians(fov)
        self.z_max = z_max
        self.z_min = z_min
        self.root = tk.Tk()
        self.root.title(nom)
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg=color)
        self.canvas.pack()
        self.position_camera = vecteur.Vecteur(0, 0, 0)
        self.look = vecteur.Vecteur(0, 0, 1)
        self.up = vecteur.Vecteur(0, 1, 0)


    def placer_point(self, vect):
        self.canvas.create_oval(vect.x-3, vect.y-3, vect.x+3, vect.y+3, fill="black")


    def placer_ligne(self, start, end):
        self.canvas.create_line(start.x,
                                start.y,
                                end.x,
                                end.y,
                                fill="black")

    def placer_triangle(self, triangle):

        origine = vecteur.addVecteurNombre(triangle.origine, 1)
        vect1 = vecteur.addVecteurNombre(triangle.vect1, 1)
        vect2 = vecteur.addVecteurNombre(triangle.vect2, 1)

        origine.x *= 0.5 * self.width
        origine.y *= 0.5 * self.height
        vect1.x *= 0.5 * self.width
        vect1.y *= 0.5 * self.height
        vect2.x *= 0.5 * self.width
        vect2.y *= 0.5 * self.height

        color_value = int(triangle.orientation.z * -255)
        if(color_value < 0):
            color_value = 0
        color = f"#{color_value:02x}{color_value:02x}{color_value:02x}"

        self.canvas.create_polygon(origine.x, origine.y,
                                   vect1.x, vect1.y,
                                   vect2.x, vect2.y,
                                   fill=color)

    def run(self):
        self.root.mainloop()